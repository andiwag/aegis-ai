from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import text

from aegis.db import check_connection, create_db_engine

BACKEND_ROOT = Path(__file__).resolve().parents[1]


def _postgres_up() -> bool:
    try:
        check_connection(create_db_engine())
        return True
    except Exception:
        return False


@pytest.mark.skipif(not _postgres_up(), reason="PostgreSQL is not running")
def test_alembic_upgrade_head() -> None:
    config = Config(str(BACKEND_ROOT / "alembic.ini"))
    command.upgrade(config, "head")
    engine = create_db_engine()
    with engine.connect() as connection:
        version = connection.execute(text("SELECT version_num FROM alembic_version")).scalar_one()
    assert version
