from typing import List

from pydantic.main import BaseModel


class Author(BaseModel):
    name: str
    book: List[str]
