from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, CheckConstraint

from .base_models import BaseModel


class OurMission(BaseModel):
    __table_args__ = (
        CheckConstraint('id = 1', name='single_contact_only'),
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    image: Mapped[str] = mapped_column(nullable=True, default='')

    def __repr__(self):
        return f"OurMission(id={self.id}, title={self.title})"
