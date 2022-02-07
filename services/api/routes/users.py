from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from db import users
from schemas.users import UserBase, UserDisplay

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=UserDisplay
)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    user = users.create_user(db, request)
    return user


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[UserDisplay]
)
def list_users(db: Session = Depends(get_db)):
    return users.get_users(db)
