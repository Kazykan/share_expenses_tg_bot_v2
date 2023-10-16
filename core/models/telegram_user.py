from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship

from .base import Base


if TYPE_CHECKING:
    from .place import Place


class TelegramUser(Base):
    __tablename__ = 'telegram_users'

    name: Mapped[str]
    id_telegram: Mapped[int]
    places: Mapped[list["Place"]] = relationship(back_populates="users")
