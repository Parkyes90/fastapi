from datetime import datetime

from fastapi import FastAPI, Depends, exceptions
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from starlette.responses import Response

from models.jwt_users import JWTUser
from routes.v1 import app_v1
from starlette.requests import Request

from routes.v2 import app_v2
from utils.security import (
    check_jwt_token,
    authenticate_user,
    create_jwt_token,
)

app = FastAPI(
    title="Bookstore API Documentation",
    description="It is API",
    version="1.0.0",
)

app.include_router(
    app_v1, prefix="/v1", dependencies=[Depends(check_jwt_token)]
)
app.include_router(
    app_v2, prefix="/v2", dependencies=[Depends(check_jwt_token)]
)


@app.post(
    "/token",
    description="사용자 이름과 비밀번호를 페이로드로 제공하면 액세스 토큰을 반환합니다",
    summary="JWT 토큰을 반환합니다.",
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    jwt_user_dict = {
        "username": form_data.username,
        "password": form_data.password,
    }
    jwt_user = JWTUser(**jwt_user_dict)
    user = authenticate_user(jwt_user)
    if user is None:
        raise exceptions.HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    return {"access_token": create_jwt_token(user)}


@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    if not any(
        word in str(request.url)
        for word in ["/token", "/docs", "/openapi.json"]
    ):
        not_valid_response = Response(
            "Unauthorized", status_code=status.HTTP_401_UNAUTHORIZED
        )
        try:
            jwt_token = request.headers["Authorization"].split(" ")[1]
            is_valid = check_jwt_token(jwt_token)
            if not is_valid:
                return not_valid_response
        except KeyError:
            return not_valid_response
    response = await call_next(request)
    execution_time = (datetime.utcnow() - start_time).microseconds
    response.headers["x-execution-time"] = str(execution_time)
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("run:app", reload=True)
