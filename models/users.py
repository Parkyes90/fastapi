from pydantic import BaseModel
import enum
from fastapi import Query


class Role(enum.Enum):
    admin = "admin"
    personal = "personal"


class User(BaseModel):
    name: str
    password: str
    mail: str = Query(..., regex=r"[\w\.-]+@[\w\.-]+(\.[\w]+)+")
    role: Role
