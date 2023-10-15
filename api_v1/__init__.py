from fastapi import APIRouter

from .telegram_user.views import router as telegram_user_router

router = APIRouter()
router.include_router(router=telegram_user_router, prefix='/telegram_users')
