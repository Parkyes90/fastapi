from fastapi import FastAPI

from db import models
from db.database import engine
from routes.blog import router as blog_router
from routes.users import router as users_router

app = FastAPI()
app.include_router(blog_router)
app.include_router(users_router)


@app.get("/")
def index():
    return {"message": "Hello World"}


models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
