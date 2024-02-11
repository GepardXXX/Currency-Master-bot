import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

env_file_path = os.path.abspath(".")


class Settings(BaseSettings):
    bot_token: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

config = Settings()

