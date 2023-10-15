from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, TelegramUser
from . import crud


async def telegram_user_by_id(
        telegram_user_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.session_dependency)
) -> TelegramUser:
    telegram_user = await crud.get_telegram_user(
        session=session,
        telegram_user_id=telegram_user_id)
    if telegram_user is not None:
        return telegram_user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Telegram user {telegram_user_id} not found!'
    )
