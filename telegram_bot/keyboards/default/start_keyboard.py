from aiogram import types


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
start_keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True
)
