from fastapi import FastAPI, Body, Header, File
from starlette.responses import Response

from models.Authors import Author
from models.books import Book
from models.users import User
from starlette import status
from starlette import exceptions

app = FastAPI()


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def post_user(user: User, x_custom: str = Header("")):
    if user is None:
        raise exceptions.HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE
        )

    return {"request body": user, "header": x_custom}


@app.get("/users")
async def get_user_validation(password: str = ""):
    return {"query": password}


@app.get(
    "/books/{isbn}",
    response_model=Book,
    response_model_exclude={"author", "name", "year"},
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


@app.get("/authors/{author}/books")
async def get_authors_books(
    author: int, category: str, order: str = "asc",
):
    return {"query": str(author) + order + category}


@app.patch("/authors/name")
async def patch_author_name(name: str = Body(..., embed=True)):
    return {"query": name}


@app.post("/users/authors")
async def post_user_and_author(
    user: User, author: Author, bookstore_name: str = Body(..., embed=True)
):
    return {"user": user, "author": author}


@app.post("/users/photo")
async def upload_user_photo(
    response: Response, profile_photo: bytes = File(...)
):
    response.headers["x-file-size"] = str(len(profile_photo))
    response.set_cookie(key="cookie-api", value="test", httponly=True)
    return {"file size": len(profile_photo)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("run:app", reload=True)
