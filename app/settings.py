from typing import Union

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='ignore', env_file="../.env",)

    mysql_db_name: Union[str, None] = None
    mysql_db_user: Union[str, None] = None
    mysql_db_password: Union[SecretStr, None] = None
    mysql_db_rootpassword: Union[SecretStr, None] = None
    mysql_db_url: Union[str, None] = None
    mysql_db_port: Union[int, None] = None
    mysql_db_host: Union[str, None] = None


def get_settings():
    return Settings()
