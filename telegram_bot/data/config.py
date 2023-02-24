from environs import Env
from dataclasses import dataclass

env = Env()
env.read_env()


@dataclass
class Settings:
    BOT_TOKEN: str
    DATABASE_CONNECTION: str


settings = Settings(
    BOT_TOKEN=env.str("BOT_TOKEN"),
    DATABASE_CONNECTION=env.str("BOT_DATABASE_CONNECTION"),
)
