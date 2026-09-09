# Aegis

Companion source for *Building Production-Grade AI Applications*.

This repository is **Aegis Core** — the production-grade platform the book builds. The book itself is a separate manuscript. You do not need this repo to read the chapters. You need it to compare your code, catch up, or inspect a checkpoint.

- Source: https://github.com/andiwag/aegis-ai
- Chapter checkpoints: git tags `book-chNN` (only chapters that change this source)

```bash
git clone https://github.com/andiwag/aegis-ai
cd aegis-ai
git checkout book-ch10
```

Core is a modular monolith: one Python package (`backend/`) with an API process and a worker process, a React app (`frontend/`), and Docker Compose at the repository root.
