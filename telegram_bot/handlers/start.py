from aiogram import types, Dispatcher
from loader import dp


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ Эхо-бот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


def register_handlers_start(dispatcher: Dispatcher):
    dispatcher.register_message_handler(send_welcome, commands=['start'])
    dispatcher.register_message_handler(echo)
# @dp.message_handler(commands=['start'])  # Явно указываем в декораторе, на какую команду реагируем.
# async def send_welcome(message: types.Message, state: FSMContext):
#     # check if user in db, if not, add user
#     # set_state, set first stats line
#     # await state.set_state(SessionCheck.start)
#     # x = await state.get_state()
#     # if x == 'SessionCheck:start':
#     # Так как код работает асинхронно, то обязательно пишем await.
#     # await message.reply(f"Привет!\nЯ твой помощник!\nОтправь мне любое сообщение, а я тебе обязательно отвечу. {x}",
#     #                     reply_markup=start_keyboard())
