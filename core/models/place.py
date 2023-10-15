from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .base import Base


class Place(Base):

    name: Mapped[str]
    telegram_user_id: Mapped[int] = mapped_column(
        ForeignKey("telegram_users.id")
        )


# class Place(Base):
#     "Название активности"
#     __tablename__ = "place"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     telegram_user_id: Mapped[List["TelegramUser"]] = relationship(
#         cascade="all, delete, delete-orphan")
