from typing import List

from pydantic import BaseModel


class Article(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleDisplay(BaseModel):
    id: int
    title: str
    published: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    articles: List[ArticleDisplay] = []

    class Config:
        orm_mode = True
