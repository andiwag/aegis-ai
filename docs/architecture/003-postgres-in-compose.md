# ADR-003: PostgreSQL in Compose

- Status: Accepted
- Date: 2026-09-10

## Context

Aegis Core needs one system of record. Chapter 4 chose PostgreSQL with pgvector. Developers must not install Postgres on the host. Liveness and readiness are different questions.

## Decision

- Run PostgreSQL via Docker Compose at the repository root, image `pgvector/pgvector` so the vector extension is available when RAG arrives. Do not enable the extension until that chapter.
- Keep `/health` as process liveness. Add `/ready` that fails when the database does not answer `SELECT 1`.
- The API process still runs on the host in development. Only the datastore is a container in this step.
- SQLAlchemy provides the engine now. Tables and Alembic wait for the models chapter.

## Consequences

`docker compose up -d` starts the database. A reader can stop Postgres and still see `/health` succeed while `/ready` returns 503. Production uses the same `DATABASE_URL` name with a different value.
