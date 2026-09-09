"""PostgreSQL engine. Schema arrives in the models chapter."""

from __future__ import annotations

import os

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

DEFAULT_DATABASE_URL = "postgresql+psycopg://aegis:aegis@127.0.0.1:5432/aegis"


def database_url() -> str:
    return os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)


def create_db_engine(url: str | None = None) -> Engine:
    return create_engine(url or database_url(), pool_pre_ping=True)


def check_connection(engine: Engine) -> None:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
