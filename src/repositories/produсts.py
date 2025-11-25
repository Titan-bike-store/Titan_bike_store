from sqlalchemy import select

from .base_reposiroty import BaseRepository
from models.products import Product, ProductGallery, Characteristics, Brand


class BrandRepository(BaseRepository):
    model = Brand


class ProductRepository(BaseRepository):
    model = Product


class ProductGalleryRepository(BaseRepository):
    model = ProductGallery

    async def get_by_id_product(self, product_id: int, *options):
        stmt = select(self.model).where(self.model.product_id == product_id)
        if options:
            stmt = stmt.options(*options)
        result = await self.db.execute(stmt)
        return result.unique().scalars().all()


class ProductCharacteristicsRepository(BaseRepository):
    model = Characteristics
