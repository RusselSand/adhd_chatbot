from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.default.start_keyboard import start_keyboard
from loader import dp


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Привет!\nЯ твой помощник!\nОтправь мне любое сообщение, а я тебе обязательно отвечу. ",
                        reply_markup=start_keyboard)


# TODO: как регистрировать
@dp.message_handler(Text(startswith="Списки"))
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Эмоции 🌋'),
            types.KeyboardButton(text='Домашние дела 🏡')
        ],
        [
            types.KeyboardButton(text='Работа/учеба 💼')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("Отличный выбор!", reply_markup=keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


def register_handlers_start(dispatcher: Dispatcher):
    dispatcher.register_message_handler(send_welcome, commands=['start'])
    dispatcher.register_message_handler(with_puree, lambda msg: msg.text.lower() == 'Списки')
    dispatcher.register_message_handler(echo)
