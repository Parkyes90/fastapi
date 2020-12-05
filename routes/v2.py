from fastapi import APIRouter

app_v2 = APIRouter()


@app_v2.get("/users")
async def get_user_validation(password: str = ""):
    return {"query": password}
