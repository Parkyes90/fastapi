from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.users import ArticleDisplay, Article, ArticleDetail
from db import articles

router = APIRouter(prefix="/articles", tags=["articles"])


@router.post("/", response_model=ArticleDisplay)
def create_article(request: Article, db: Session = Depends(get_db)):
    return articles.create_article(db, request)


@router.get(
    "/{article_id}",
    status_code=status.HTTP_200_OK,
    response_model=ArticleDetail,
)
def retrieve_article(article_id: int, db: Session = Depends(get_db)):
    return articles.get_article(db, article_id)
