from sqlalchemy.orm import Session

from db.models import User
from schemas.users import UserBase
from db.utils import PasswordHash


def create_user(db: Session, request: UserBase):
    new_user = User(
        username=request.username,
        email=request.email,
        password=PasswordHash(request.password).bcrypt(),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
