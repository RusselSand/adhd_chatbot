from aiogram import Bot, Dispatcher, executor, types, utils
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from telegram_bot.session_check import SessionCheck


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


@dp.message_handler(Text("Списки 📋"))
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


# ToDo: посмотреть, можно ли сделать сообщения регистронезависимыми
@dp.message_handler(Text(startswith="Эмоции"))
async def with_puree(message: types.Message):
    buttons = [
        [
            types.InlineKeyboardButton(text='Злость', callback_data="emotion_angry"),
            types.InlineKeyboardButton(text='Грусть',  callback_data="emotion_sad")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.reply("Выбери эмоцию, которая тебе сейчас ближе всего: ", reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith="emotion_"))
async def callbacks_num(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]
    if action == "angry":
        text = """
        Если я раздражён/зол: 
        1. Оставить дело, которым я занимаюсь, сразу. 
        2. Подумать, какая моя потребность не удовлетворяется сейчас
        3. Сказать об этом, если мне могут помочь. 
        4. Взять паузу 5-10 минут, чтобы успокоиться. Прогуляться, попить воды, полежать, порвать пакет. 
        5. Найти решение одному или вместе.
        """
        await bot.send_message(callback.from_user.id, text)
        #await message.reply("Выбери эмоцию, которая тебе сейчас ближе всего: злость")
    # elif action == "sad":
        #await message.reply("Выбери эмоцию, которая тебе сейчас ближе всего: печаль")


@dp.message_handler()
# Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message):
    # Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
