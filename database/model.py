import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  Column, Integer, String, create_engine
from typing import List

from sqlalchemy import MetaData, Table, Column, Integer, String, \
    ForeignKey, Float, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase, \
    Mapped, mapped_column

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
    )


# Base = declarative_base()


# class Person(Base):
#     __tablename__ = "people"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     age = Column(Integer,)


class Base(DeclarativeBase):
    pass


class Person(Base):
    """Пользователь"""
    __tablename__ = 'people'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)


class User(Base):
    """Пользователь"""
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    id_telegram: Mapped[int] = mapped_column(Integer, nullable=True)
    place_id: Mapped[List["Place"]] = relationship()


class Place(Base):
    "Название активности"
    __tablename__ = "place"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    telegram_user_id: Mapped[List["TelegramUser"]] = relationship(
        cascade="all, delete, delete-orphan")


class TelegramUser(Base):
    """Телеграмм пользователь"""
    __tablename__ = "telegram_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    id_telegram: Mapped[int] = mapped_column(Integer)


class Expense(Base):
    """Расход"""
    __tablename__ = 'expense'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    cost: Mapped[float] = mapped_column(Float)
    date: Mapped[datetime.date] = mapped_column(Date)
    who_paid_user_id: Mapped[List["User"]] = relationship()
    place_id: Mapped[List["Place"]] = relationship()


class MoneyTransfer(Base):
    """Перевод денег"""
    __tablename__ = "money_transfer"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(Float)
    who_paid_user_id: Mapped[List["User"]] = relationship()
    who_gets_user_id: Mapped[List["User"]] = relationship()
    date: Mapped[datetime.date] = mapped_column(Date)
    place_id: Mapped[List["Place"]] = relationship()


SessionLocal = sessionmaker(autoflush=False, bind=engine)






# import datetime
# from typing import List

# from sqlalchemy import MetaData, Table, Column, Integer, String, \
#     ForeignKey, Float, Date
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase, \
#     Mapped, mapped_column


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False})


# class Base(DeclarativeBase):
#     pass


# class User(Base):
#     """Пользователь"""
#     __tablename__ = 'user'

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     id_telegram: Mapped[int] = mapped_column(Integer, nullable=True)
#     # place_id: Mapped[List["Activity"]] = relationship()


# SessionLocal = sessionmaker(autoflush=False, bind=engine)

# user = Table(
#     'user',
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("id_telegram", Integer, nullable=True),
#     Column("place_id", Integer, ForeignKey("place.id", ondelete='CASCADE'))
# )


# place = Table(
#     'place',
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("telegram_user_id", Integer,
#            ForeignKey("telegram_user.id", ondelete='CASCADE'))
# )

# expanse = Table(
#     'expanse',
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("cost", Float, nullable=False),
#     Column("date", Date, nullable=False),
#     Column("who_paid_user_id", ForeignKey("user.id", ondelete="CASCADE")),
#     Column("place_id", Integer, ForeignKey("place.id", ondelete="CASCADE"))
# )

# money_transfer = Table(
#     'money_transfer',
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("date", Date, nullable=False),
#     Column("amount", Float, nullable=False),
#     Column("who_paid_user_id", ForeignKey("user.id", ondelete="CASCADE")),
#     Column("who_gets_user_id", ForeignKey("user.id", ondelete="CASCADE")),
#     Column("place_id", ForeignKey("user.id", ondelete="CASCADE"))
# )

# telegram_user = Table(
#     'telegram_user',
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("id_telegram", Integer, nullable=False)
# )