from fastapi import Body, File, APIRouter
from starlette.responses import Response

from models.authors import Author
from models.books import Book
from models.users import User
from starlette import status
from starlette import exceptions

app_v1 = APIRouter()


@app_v1.post("/users", status_code=status.HTTP_201_CREATED, tags=["users"])
async def post_user(user: User):
    if user is None:
        raise exceptions.HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE
        )

    return {"request body": user}


@app_v1.get("/users", tags=["users"])
async def get_user_validation(password: str = ""):
    return {"query": password}


@app_v1.get(
    "/books/{isbn}",
    response_model=Book,
    response_model_exclude={"author", "name", "year"},
    tags=["books"],
)
async def get_book_with_isbn(isbn: str):
    author_dict = {"name": "author1", "book": ["book1", "book2"]}
    author1 = Author(**author_dict)
    book_dict = {
        "isbn": "isbn1",
        "name": "book1",
        "year": 2019,
        "author": author1,
    }
    book1 = Book(**book_dict)
    return book1


@app_v1.get(
    "/authors/{author}/books", tags=["books"],
)
async def get_authors_books(
    author: int, category: str, order: str = "asc",
):
    return {"query": str(author) + order + category}


@app_v1.patch("/authors/name")
async def patch_author_name(name: str = Body(..., embed=True)):
    return {"query": name}


@app_v1.post("/users/authors")
async def post_user_and_author(
    user: User, author: Author, bookstore_name: str = Body(..., embed=True)
):
    return {"user": user, "author": author}


@app_v1.post("/users/photo")
async def upload_user_photo(
    response: Response, profile_photo: bytes = File(...)
):
    response.headers["x-file-size"] = str(len(profile_photo))
    response.set_cookie(key="cookie-api", value="test", httponly=True)
    return {"file size": len(profile_photo)}
