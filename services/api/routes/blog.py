from typing import Optional, List

from fastapi import APIRouter, Response, status, Query, Body, Path

from schemas.blog import BlogType, BlogModel, ResponseModel

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get("/{blog_id}/comments/{comment_id}", tags=["comments"])
def get_comment(
    blog_id: int,
    comment_id: int,
    valid: bool = True,
    username: Optional[str] = None,
):
    """
    Simulates retrieving a comment of a blog
    - :param blog_id: mandatory path parameter
    - :param comment_id: mandatory path parameter
    - :param valid: optional query parameter
    - :param username: optional query parameter
    - :return: string
    """
    return {
        "message": f"blog_id {blog_id}, comment_id {comment_id}, valid {valid}, username: {username}"
    }


@router.get("/type/{blog_type}")
def get_blog_type(blog_type: BlogType):
    return {"message": f"Blog type {blog_type}"}


@router.get(
    "/{blog_id}",
    status_code=status.HTTP_200_OK,
)
def get_blog(blog_id: int, response: Response):
    if blog_id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {blog_id} not found"}
    return {"message": f"Blog with id {blog_id}"}


@router.get(
    "",
    summary="Retrieve all blogs",
    description="This api call simulates fetching all blogs",
    response_description="The list of blogs",
)
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@router.post(
    "",
    response_model=ResponseModel[BlogModel],
)
def create_blog(blog: BlogModel):
    return ResponseModel[BlogModel](data=blog)


@router.post("/{blog_id}/comments", tags=["comments"])
def create_comment(
    blog_id: int = Path(None, gt=5, lt=10),
    comment_content: str = Query(
        None,
        title="content of content",
        description="Some description",
        alias="commentContent",
        deprecated=True,
    ),
    content: str = Body(..., min_length=10, regex="^[a-z\\s]*$"),
    v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"]),
):
    return {"blog_id": blog_id, "content": content, "version": v}
