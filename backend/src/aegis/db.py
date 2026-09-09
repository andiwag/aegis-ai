"""PostgreSQL engine, sessions, and declarative base."""

from __future__ import annotations

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from aegis.settings import get_settings


class Base(DeclarativeBase):
    pass


def create_db_engine(url: str | None = None) -> Engine:
    return create_engine(url or get_settings().database_url, pool_pre_ping=True)


def create_session_factory(engine: Engine) -> sessionmaker[Session]:
    return sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def check_connection(engine: Engine) -> None:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
