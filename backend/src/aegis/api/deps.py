"""FastAPI dependencies."""

from __future__ import annotations

from collections.abc import Iterator

from fastapi import Request
from sqlalchemy.orm import Session


def get_db(request: Request) -> Iterator[Session]:
    session = request.app.state.SessionLocal()
    try:
        yield session
    finally:
        session.close()
