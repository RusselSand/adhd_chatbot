from aiogram import executor
from data.config import settings
from loader import dp
from utils.db_connect.models import db
from handlers import start


async def on_startup(dispatcher):
    print("Бот вышел в онлайн")
    await db.set_bind(settings.DATABASE_CONNECTION)


async def on_shutdown(dispatcher):
    await db.pop_bind().close()


if __name__ == '__main__':
    start.register_handlers_start(dp)
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)

# async def set_default_commands(dp):
#     await dp.bot.set_my_commands(
#         [
#             types.BotCommand("start", "Botni ishga tushurish"),
#             types.BotCommand("help", "Yordam"),
#         ]
#     )