from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from typing import List
from slugify import slugify

from .base_models import BaseModel
from .association_tables import category_product


class Brand(BaseModel):
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(nullable=True)
    product: Mapped[List["Product"]] = relationship(back_populates="brand")

    def __init__(self, **kw):
        super().__init__(**kw)
        if not self.slug and self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f"<Brand(id={self.id}, title={self.title})>"


class Product(BaseModel):
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(1000))
    price: Mapped[int] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    slug: Mapped[str] = mapped_column(nullable=True)
    characteristics: Mapped[List["Characteristics"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )
    gallery: Mapped[List["ProductGallery"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )
    categories: Mapped[List['Category']] = relationship(
        secondary=category_product,
        back_populates='products'
    )
    brand_id: Mapped[int] = mapped_column(
        ForeignKey("brands.id", ondelete="SET NULL"),
        nullable=True
    )
    brand: Mapped["Brand"] = relationship(
        back_populates="product"
    )

    def __init__(self, **kw):
        super().__init__(**kw)
        if not self.slug and self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f"<Product(id={self.id}, title={self.title})>"


class ProductGallery(BaseModel):
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="gallery")
    file: Mapped[str] = mapped_column(nullable=True, default='')

    def __repr__(self):
        return f"<ProductGallery(id={self.id}, title={self.product.title})>"


class Characteristics(BaseModel):
    name: Mapped[str] = mapped_column(String(255))
    value: Mapped[str] = mapped_column(String(255))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="characteristics")

    def __repr__(self):
        return f"<Characteristic(id={self.id}, name={self.name})>"
