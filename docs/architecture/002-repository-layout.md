# ADR-002: Repository layout

- Status: Accepted
- Date: 2026-09-09

## Context

The companion git repository is Aegis Core source, not the book manuscript. API and worker must share one Python package. The UI is a second artifact. Compose must wire every process.

## Decision

One git repository:

- `backend/` — installable package `aegis` (`src/` layout), entrypoints `aegis.api` and `aegis.worker`
- `frontend/` — React app
- `compose.yaml` at the repository root
- `.env` gitignored; `.env.example` committed
- ADRs in `docs/architecture/`

Domain modules are added when implemented, not as empty folders.

## Consequences

One clone, one CI later, one Compose file. Frontend still talks to the API over HTTP only.
