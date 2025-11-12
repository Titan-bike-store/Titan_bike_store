from sqlalchemy import select

from .base_reposiroty import BaseRepository
from models.users import User


class UserRepository(BaseRepository):
    model = User

    async def get_user_by_telegram_id(self, telegram_id: int, *options):
        stmt = select(self.model).where(self.model.telegram_id == telegram_id)
        if options:
            stmt = stmt.options(*options)
        user = await self.db.execute(stmt)
        return user.scalar_one_or_none()

    async def get_user_by_username(self, username: str, *options):
        stmt = select(self.model).where(self.model.username == username)
        if options:
            stmt = stmt.options(*options)
        user = await self.db.execute(stmt)
        return user.scalar_one_or_none()
