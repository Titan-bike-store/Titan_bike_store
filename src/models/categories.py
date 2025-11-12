from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from slugify import slugify
from typing import List

from .base_models import BaseModel
from .association_tables import category_product


class Category(BaseModel):
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(nullable=True)
    products: Mapped[List['Product']] = relationship(
        secondary=category_product,
        back_populates="categories"
    )

    def __init__(self, **kw):
        super().__init__(**kw)
        if not self.slug and self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f"<Category(id={self.id}, title={self.title})>"
