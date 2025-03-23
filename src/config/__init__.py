"""Settings package."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App settings."""

    redis_endpoint: str = Field(validation_alias="REDIS_ENDPOINT")
    redis_port: int = Field(validation_alias="REDIS_PORT")
    redis_password: str = Field(validation_alias="REDIS_PASSWORD")

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    """Return app settings."""
    return Settings()


settings = get_settings()
