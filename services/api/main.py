from fastapi import FastAPI
from routers.blog import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def index():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
