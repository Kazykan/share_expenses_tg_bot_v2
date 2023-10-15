"""
Create
Read
Update
Delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import TelegramUser
from .schemas import TelegramUserCreate, TelegramUserUpdate, \
     TelegramUserUpdatePartial


async def get_telegram_users(session: AsyncSession) -> list[TelegramUser]:
    stmt = select(TelegramUser).order_by(TelegramUser.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_telegram_user(
        session: AsyncSession, telegram_user_id: int) -> TelegramUser | None:
    return await session.get(TelegramUser, telegram_user_id)


async def create_telegram_user(
        session: AsyncSession,
        telegram_user_in: TelegramUserCreate) -> TelegramUser:
    telegram_user = TelegramUser(**telegram_user_in.model_dump())
    session.add(telegram_user)
    await session.commit()
    return telegram_user


async def update_telegram_user(
        session: AsyncSession,
        telegram_user: TelegramUser,
        telegram_user_update: TelegramUserUpdate | TelegramUserUpdatePartial,
        partial: bool = False
) -> TelegramUser:
    for name, value in telegram_user_update.model_dump(
            exclude_unset=partial).items():
        setattr(telegram_user, name, value)
        await session.commit()
        return telegram_user


async def delete_telegram_user(
        session: AsyncSession,
        telegram_user: TelegramUser) -> None:
    await session.delete(telegram_user)
    # await session.commit()
