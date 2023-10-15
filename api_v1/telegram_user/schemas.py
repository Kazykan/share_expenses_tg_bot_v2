from pydantic import BaseModel, ConfigDict


class TelegramUserBase(BaseModel):
    name: str
    id_telegram: int


class TelegramUserCreate(TelegramUserBase):
    pass


class TelegramUserUpdate(TelegramUserCreate):
    pass


class TelegramUserUpdatePartial(TelegramUserUpdate):
    name: str | None = None
    id_telegram: int | None = None


class TelegramUserSchema(TelegramUserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
