import datetime

from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


def make_plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word.endswith(('s', 'sh', 'ch', 'x', 'z')):
        return word + 'es'
    elif word.endswith('f'):
        return word[:-1] + 'ves'
    elif word.endswith('fe'):
        return word[:-2] + 'ves'
    else:
        return word + 's'


class BaseModel(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return make_plural(cls.__name__.lower())

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('Asia/Bishkek', now())"), nullable=True
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('Asia/Bishkek', now())"),
        onupdate=text("TIMEZONE('Asia/Bishkek', now())"),
        nullable=True
    )
