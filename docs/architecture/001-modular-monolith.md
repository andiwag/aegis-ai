# ADR-001: Modular monolith

- Status: Accepted
- Date: 2026-09-09

## Context

Aegis Core needs a browser UI, an HTTP API, background ingestion, and a path to Enterprise modules, run by a small team and on Docker Desktop.

## Decision

One API process with internal domain modules (in-process calls). A second process for jobs, same codebase. Not microservices. Not a ball of mud.

Tenancy: shared database, `organization_id` on tenant-owned rows, enforced in API and worker.

Model access: a Model Gateway *module* imported by API and worker, not a separate service.

## Consequences

We scale with more workers and a larger database until a module has a genuinely different lifecycle. Enterprise adds modules behind the same seams.
