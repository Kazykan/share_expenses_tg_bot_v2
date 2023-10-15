from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import TelegramUserSchema, TelegramUserCreate, \
    TelegramUserUpdate, TelegramUserUpdatePartial
from .dependencies import telegram_user_by_id

router = APIRouter(tags=["TelegramUser"])


@router.get('/', response_model=list[TelegramUserSchema])
async def get_telegram_users(
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_telegram_users(session=session)


@router.post('/', response_model=TelegramUserSchema,
             status_code=status.HTTP_201_CREATED)
async def create_telegram_user(
        telegram_user_in: TelegramUserCreate,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_telegram_user(
        session=session,
        telegram_user_in=telegram_user_in)


@router.get('/{telegram_user_id}/', response_model=TelegramUserSchema)
async def get_telegram_user(
        telegram_user: TelegramUserSchema = Depends(telegram_user_by_id)):
    return telegram_user


@router.put('/{telegram_user_id}/')
async def update_telegram_user(
    telegram_user_update: TelegramUserUpdate,
    telegram_user: TelegramUserSchema = Depends(telegram_user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_telegram_user(
        session=session,
        telegram_user=telegram_user,
        telegram_user_update=telegram_user_update,
    )


@router.patch('/{telegram_user_id}/')
async def update_telegram_user_partial(
    telegram_user_update: TelegramUserUpdatePartial,
    telegram_user: TelegramUserSchema = Depends(telegram_user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_telegram_user(
        session=session,
        telegram_user=telegram_user,
        telegram_user_update=telegram_user_update,
        partial=True,
    )


@router.delete('/{telegram_user_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_telegram_user(
    telegram_user: TelegramUserSchema = Depends(telegram_user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_telegram_user(
        session=session,
        telegram_user=telegram_user
    )
