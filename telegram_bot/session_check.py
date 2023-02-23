from aiogram.dispatcher.filters.state import State, StatesGroup


class SessionCheck(StatesGroup):
    start = State()
    settings = State()
