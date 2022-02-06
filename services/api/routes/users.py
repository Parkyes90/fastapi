from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db import users
from schemas.users import UserBase

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return users.create_user(db, request)
