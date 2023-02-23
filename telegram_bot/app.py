from aiogram import executor
from loader import dp
from aiogram import Bot, Dispatcher, executor, types, utils
from aiogram.dispatcher import FSMContext

from session_check import SessionCheck


@dp.message_handler(commands=['start'])  # Явно указываем в декораторе, на какую команду реагируем.
async def send_welcome(message: types.Message, state: FSMContext):
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
    await state.set_state(SessionCheck.start)
    x = await state.get_state()
    if x == 'SessionCheck:start':
    # Так как код работает асинхронно, то обязательно пишем await.
        await message.reply(f"Привет!\nЯ твой помощник!\nОтправь мне любое сообщение, а я тебе обязательно отвечу. {x}",
                        reply_markup=keyboard)
    else:
        await message.reply(f"Пока!\nЯ твой помощник!\nОтправь мне любое сообщение, а я тебе обязательно отвечу. {x}",
                        reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)