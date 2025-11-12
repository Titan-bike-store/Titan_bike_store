from sqlalchemy.orm import mapped_column, Mapped

from .base_models import BaseModel


class User(BaseModel):
    telegram_id: Mapped[int] = mapped_column(unique=True, nullable=True, default=1)
    username: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    first_name: Mapped[str] = mapped_column(nullable=True, default='')
    last_name: Mapped[str] = mapped_column(nullable=True, default='')
    password: Mapped[str] = mapped_column(nullable=True, default='')

    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"
