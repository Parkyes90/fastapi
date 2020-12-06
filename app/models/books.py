from pydantic import BaseModel, Schema

from .authors import Author


class Book(BaseModel):
    isbn: str = Schema(None, description="It is unique identification")
    name: str
    author: Author
    year: int = Schema(None, gt=1900, lt=2100)
