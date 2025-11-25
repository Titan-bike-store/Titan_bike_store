from typing import List
from sqlalchemy import select

from .base_reposiroty import BaseRepository
from models.categories import Category


class CategoryRepository(BaseRepository):
    model = Category

    async def get_by_ids(self, ids: List[int],  *options):
        if not ids:
            return []
        stmt = select(self.model).where(self.model.id.in_(ids))
        if options:
            stmt = stmt.options(*options)
        result = await self.db.execute(stmt)
        return result.unique().scalars().all()
