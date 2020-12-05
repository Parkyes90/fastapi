from pydantic.main import BaseModel


class JWTUser(BaseModel):
    username: str
    password: str
    disabled: bool = False
    role: str = None
