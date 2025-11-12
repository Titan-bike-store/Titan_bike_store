from sqlalchemy import Table, Column, ForeignKey
from .base_models import BaseModel


category_product = Table(
    "category_product",
    BaseModel.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True)
)
