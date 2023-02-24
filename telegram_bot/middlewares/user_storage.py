from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from services.user import get_or_create_user


class UserStorageMiddleware(BaseMiddleware):
    def __init__(self, database):
        self.database = database
        super().__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        user = message.from_user
        db_user, _created = await get_or_create_user(
            user_id=user.id,
            user_account=user.username
        )
        data['user'] = db_user
