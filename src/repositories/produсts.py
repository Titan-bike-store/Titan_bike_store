from .base_reposiroty import BaseRepository
from models.products import Product, ProductImage, Characteristics


class ProductRepository(BaseRepository):
    model = Product


class ProductImageRepository(BaseRepository):
    model = ProductImage


class ProductCharacteristicsRepository(BaseRepository):
    model = Characteristics
