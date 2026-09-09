"""Process settings from the environment."""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_DATABASE_URL = "postgresql+psycopg://aegis:aegis@127.0.0.1:5432/aegis"
DEFAULT_CORS_ORIGINS = "http://127.0.0.1:5173,http://localhost:5173"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "../.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: str = DEFAULT_DATABASE_URL
    cors_origins: str = DEFAULT_CORS_ORIGINS

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
