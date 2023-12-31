from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, \
    declared_attr


class Base(DeclarativeBase):
    """Базовая модель с ней мы ничего не делаем"""
    __abstract__ = True

    # чтобы у моделей не писать __tablename__ = 'имя таблицы'
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'

    id: Mapped[int] = mapped_column(primary_key=True)
