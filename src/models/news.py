from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from typing import List
from slugify import slugify


from .base_models import BaseModel


class News(BaseModel):
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    slug: Mapped[str] = mapped_column(nullable=True)
    comments: Mapped[List["NewsComment"]] = relationship(
        back_populates="news",
        cascade="all, delete-orphan"
    )

    def __init__(self, **kw):
        super().__init__(**kw)
        if not self.slug and self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f"<News(id={self.id}, title={self.title})>"


class NewsComment(BaseModel):
    comment: Mapped[str] = mapped_column(nullable=False)
    news_id: Mapped[int] = mapped_column(ForeignKey("newses.id"))
    news: Mapped["News"] = relationship(
        back_populates="comments"
    )
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(
        back_populates="comments"
    )

    def __repr__(self):
        return f"NewsComment(id={self.id}, comment={self.comment}, news={self.news.title}, author={self.author.full_name})"
