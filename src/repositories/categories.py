from .base_reposiroty import BaseRepository
from models.categories import Category


class CategoryRepository(BaseRepository):
    model = Category
