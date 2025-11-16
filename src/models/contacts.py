from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import CheckConstraint
from .base_models import BaseModel


class Contact(BaseModel):
    __table_args__ = (
        CheckConstraint('id = 1', name='single_contact_only'),
    )
    address: Mapped[str] = mapped_column(nullable=True, default='Адрес не указан')
    phone: Mapped[str] = mapped_column(nullable=True, default='Номер телефона не указан')
    email: Mapped[str] = mapped_column(nullable=True, default='Почта не указана')
    telegram_news_channel: Mapped[str] = mapped_column(nullable=True, default='Телеграм канал не указан')
    telegram_bot: Mapped[str] = mapped_column(nullable=True, default='Телеграм бот не указан')

    def __repr__(self):
        return f"Contact(id={self.id})"
