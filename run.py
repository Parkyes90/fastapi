from fastapi import FastAPI

from routes.v1 import app_v1

app = FastAPI()

app.mount("/v1", app_v1)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("run:app", reload=True)
