'''
Contains configuration settings, usually loaded from environment variables.
'''
from typing import Union
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='ignore', env_file="../.env",)

    MYSQL_DB_NAME: Union[str, None] = None
    MYSQL_DB_USER: Union[str, None] = None
    MYSQL_DB_PASSWORD: Union[SecretStr, None] = None
    MYSQL_DB_ROOTPASSWORD: Union[SecretStr, None] = None
    MYSQL_DB_PORT: Union[int, None] = None
    MYSQL_DB_HOST: Union[str, None] = None
    MYSQL_DB_URL: Union[str, None] = None


@lru_cache
def get_settings():
    return Settings()
