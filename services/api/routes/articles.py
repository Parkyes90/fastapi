from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.users import ArticleDisplay, Article
from db import articles

router = APIRouter(prefix="/article", tags=["article"])


@router.post("/", response_model=ArticleDisplay)
def create_article(request: Article, db: Session = Depends(get_db)):
    return articles.create_article(db, request)
