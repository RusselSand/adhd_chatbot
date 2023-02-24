import uuid
from utils.db_connect.models import User


async def get_or_create_user(user_id: int, user_account: str) -> (User, bool):
    created = False
    user = await User.query.where(User.user_account == user_account).gino.first()
    if not user:
        user = await User.create(
            user_id=str(uuid.uuid4()),
            user_telegram_id=user_id,
            user_account=user_account
        )
        created = True
    return user, created
