from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello world123"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
