from sqlalchemy.orm import Mapped

from .base import Base


class TelegramUser(Base):
    __tablename__ = 'telegram_users'

    name: Mapped[str]
    id_telegram: Mapped[int]
