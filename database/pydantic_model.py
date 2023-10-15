from pydantic import BaseModel


class TelegramUserBase(BaseModel):
    name: int
    id_telegram: int


class TelegramUser(TelegramUserBase):
    id: int


