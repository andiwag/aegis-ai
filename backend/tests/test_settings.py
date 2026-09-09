from aegis.api.app import create_app
from aegis.db import Base
from aegis.settings import get_settings


def test_cors_origins_parse_from_env(monkeypatch) -> None:
    monkeypatch.setenv(
        "CORS_ORIGINS",
        "http://app.example, http://localhost:5173",
    )
    settings = get_settings()
    assert settings.cors_origin_list == [
        "http://app.example",
        "http://localhost:5173",
    ]


def test_database_url_from_env(monkeypatch) -> None:
    monkeypatch.setenv(
        "DATABASE_URL",
        "postgresql+psycopg://user:pass@db:5432/aegis",
    )
    assert get_settings().database_url == "postgresql+psycopg://user:pass@db:5432/aegis"


def test_app_session_factory_binds_engine() -> None:
    app = create_app()
    session = app.state.SessionLocal()
    try:
        assert session.bind is app.state.engine
    finally:
        session.close()


def test_base_metadata_starts_empty() -> None:
    assert list(Base.metadata.tables) == []
