"""
Copyright 2024 Jath Palasubramaniam
Licenced under the AGPLv3
"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Configuration variables
    """

    server_name: str

    db_connection: str

    model_config = SettingsConfigDict(env_file=".env")
