from aiogram import types


def start_keyboard():
    kb = [
        [
            types.KeyboardButton(text='С чего начать❓'),
            types.KeyboardButton(text='Списки 📋')
        ],
        [
            types.KeyboardButton(text='Книжки 📚'),
            types.KeyboardButton(text='Планировщик ⏰')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
