from enum import Enum
from typing import Optional, Generic, TypeVar, List, Dict

from pydantic import BaseModel, validator
from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class Error(BaseModel):
    code: int
    message: str


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key1": "val1"}


class ResponseModel(GenericModel, Generic[DataT]):
    data: Optional[DataT]
    error: Optional[Error]

    @classmethod
    @validator("error", always=True)
    def check_consistency(cls, v, values):
        if v is not None and values["data"] is not None:
            raise ValueError("must not provide both data and error")
        if v is None and values.get("data") is None:
            raise ValueError("must provide data or error")
        return v
