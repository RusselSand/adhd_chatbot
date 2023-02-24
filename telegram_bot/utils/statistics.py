from aiogram.dispatcher import FSMContext
import uuid


def check_session(previous_step, current_step, user_step):
    if previous_step == user_step:
        # все окей, это та же сессия, записываем новый шаг
        pass
    else:
        session_id = uuid.uuid4()
        pass
        # сессия новая, создаем идентификатор, сохраняем его, записываем шаг
