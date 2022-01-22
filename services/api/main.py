from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/blog/all")
def get_all_blogs():
    return {"message": "All blogs"}


@app.get("/blog/type/{blog_type}")
def get_blog_type(blog_type: BlogType):
    return {"message": f"Blog type {blog_type}"}


@app.get("/blog/{blog_id}")
def get_blog(blog_id: int):
    return {"message": f"Blog with id {blog_id}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
