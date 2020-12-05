from datetime import datetime

from fastapi import FastAPI
from starlette import status
from starlette.responses import Response

from routes.v1 import app_v1
from starlette.requests import Request

from utils.security import check_jwt_token

app = FastAPI()

app.mount("/v1", app_v1)


@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    if not str(request.url).__contains__("/token"):
        jwt_token = request.headers["Authorization"].split(" ")[1]
        is_valid = check_jwt_token(jwt_token)
        if not is_valid:
            return Response(
                "Unauthorized", status_code=status.HTTP_401_UNAUTHORIZED
            )
    response = await call_next(request)
    execution_time = (datetime.utcnow() - start_time).microseconds
    response.headers["x-execution-time"] = str(execution_time)
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("run:app", reload=True)
