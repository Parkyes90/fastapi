from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db import models
from schemas.users import Article
from utils.exceptions import StoryException


def create_article(db: Session, request: Article):
    if request.content.startswith("Once upon a time"):
        raise StoryException("No stories please")

    new_article = models.Article(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id,
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, article_id: int):
    article = (
        db.query(models.Article)
        .filter(models.Article.id == article_id)
        .first()
    )

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {article_id} not found",
        )

    return article
