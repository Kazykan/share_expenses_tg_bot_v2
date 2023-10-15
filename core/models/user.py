from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from sqlalchemy import String, ForeignKey, Integer


class User(Base):
    username: Mapped[str] = mapped_column(String(20))
    id_telegram: Mapped[int] = mapped_column(
        Integer,
        unique=False,
        nullable=True
    )
    place_id: Mapped[int] = mapped_column(
        ForeignKey("places.id")
    )
