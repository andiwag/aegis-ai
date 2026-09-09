# ADR-004: Schema migrations and process settings

- Status: Accepted
- Date: 2026-09-10

## Context

The API can reach PostgreSQL. It has no schema we can review in git. Environment variables are read with `os.getenv` in more than one module.

## Decision

- SQLAlchemy `DeclarativeBase` (`aegis.db.Base`) is the single metadata. Domain modules declare tables against it. `aegis.models` imports those modules so Alembic sees a complete `Base.metadata`.
- Alembic, run from `backend/`, is the only way the schema changes. Autogenerate is the default; we edit the revision if it is wrong. We do not apply GUI schema changes.
- Process settings live in `aegis.settings.Settings` (pydantic-settings). `DATABASE_URL` and `CORS_ORIGINS` are the first fields. Optional `.env` files (`backend/.env` or repo-root `.env`) load locally; production injects the same names.
- Identity tables wait for the auth chapter. The first revision is empty on purpose so `alembic upgrade head` exists now.

## Consequences

`uv run alembic upgrade head` is part of bringing the database up. New tables are a new revision, not a side effect of boot. Settings are one object tests can override through the environment.
