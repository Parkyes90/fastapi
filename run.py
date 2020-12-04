from fastapi import FastAPI, Body

from models.Authors import Author
from models.users import User

app = FastAPI()


@app.post("/users")
async def post_user(user: User):
    return {"request body": user}


@app.get("/users")
async def get_user_validation(password: str = ""):
    return {"query": password}


@app.get("/books/{isbn}")
async def get_book_with_isbn(isbn: str):
    return {"query": isbn}


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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("run:app", reload=True)
