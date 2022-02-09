from sqlalchemy.orm import Session

from db import models
from schemas.users import Article


def create_article(db: Session, request: Article):
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
