from .base_reposiroty import BaseRepository
from models.products import Product, ProductGallery, Characteristics


class ProductRepository(BaseRepository):
    model = Product


class ProductGalleryRepository(BaseRepository):
    model = ProductGallery


class ProductCharacteristicsRepository(BaseRepository):
    model = Characteristics
