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


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, request: UserBase):
    user = db.query(User).filter(User.id == user_id)
    user.update(
        {
            User.username: request.username,
            User.email: request.email,
            User.password: PasswordHash(request.password).bcrypt(),
        }
    )
    db.commit()
    return user.first()


def destroy_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
