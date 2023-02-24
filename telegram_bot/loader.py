from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import settings
from middlewares import user_storage
from utils.db_connect.models import db

# ToDo: what is parse mode for bot.py


bot = Bot(token=settings.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(user_storage.UserStorageMiddleware(database=db))
