from typing import Optional

from fastapi import FastAPI, Response, status
from enum import Enum


app = FastAPI()


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/blogs/{blog_id}/comments/{comment_id}")
def get_comment(
    blog_id: int,
    comment_id: int,
    valid: bool = True,
    username: Optional[str] = None,
):
    return {
        "message": f"blog_id {blog_id}, comment_id {comment_id}, valid {valid}, username: {username}"
    }


@app.get("/blogs/type/{blog_type}")
def get_blog_type(blog_type: BlogType):
    return {"message": f"Blog type {blog_type}"}


@app.get("/blogs/{blog_id}", status_code=status.HTTP_200_OK)
def get_blog(blog_id: int, response: Response):
    if blog_id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {blog_id} not found"}
    return {"message": f"Blog with id {blog_id}"}


@app.get("/blogs")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
