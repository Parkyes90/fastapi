from fastapi import FastAPI

from db import models
from db.database import engine
from routes.blog import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def index():
    return {"message": "Hello World"}


models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
