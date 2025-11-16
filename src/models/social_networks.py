from slugify import slugify
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

from .base_models import BaseModel


class SocialNetwork(BaseModel):
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(nullable=True)
    link: Mapped[str] = mapped_column(nullable=True)

    def __init__(self, **kw):
        super().__init__(**kw)
        if not self.slug and self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f"<SocialNetwork(id={self.id}, title={self.title})>"
