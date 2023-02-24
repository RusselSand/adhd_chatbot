import uuid

from utils.db_connect.models import User


async def add_user(user_account: str) -> 'User':
    return await User.create(
        user_id=uuid.uuid4(),
        user_account=user_account
    )
