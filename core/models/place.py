from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from .base import Base


# Защита от циклического импорта, мы спрашиваем сейчас идет проверка типов, а
# не выполнение кода, тогда импортировать
if TYPE_CHECKING:
    from .telegram_user import TelegramUser

class Place(Base):

    name: Mapped[str]
    telegram_user_id: Mapped[int] = mapped_column(
        ForeignKey("telegram_users.id")
        )
    telegram_user: Mapped["TelegramUser"] = relationship(
        back_populates="places")

# class Place(Base):
#     "Название активности"
#     __tablename__ = "place"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     telegram_user_id: Mapped[List["TelegramUser"]] = relationship(
#         cascade="all, delete, delete-orphan")
