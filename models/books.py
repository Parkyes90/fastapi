from pydantic import BaseModel

from models.Authors import Author


class Book(BaseModel):
    isbn: str
    name: str
    author: Author
    year: int
