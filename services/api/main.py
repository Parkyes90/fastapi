from fastapi import FastAPI, Request, responses, status

from db import models
from db.database import engine
from routes.blog import router as blog_router
from routes.users import router as users_router
from routes.articles import router as articles_router
from utils.exceptions import StoryException

app = FastAPI()
app.include_router(blog_router)
app.include_router(users_router)
app.include_router(articles_router)


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return responses.JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT, content={"detail": exc.name}
    )


models.Base.metadata.create_all(engine)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
