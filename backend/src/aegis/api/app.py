"""FastAPI application factory."""

from __future__ import annotations

import os
import uuid

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response

REQUEST_ID_HEADER = "X-Request-ID"
DEFAULT_CORS_ORIGINS = "http://127.0.0.1:5173,http://localhost:5173"


def _cors_origins() -> list[str]:
    raw = os.getenv("CORS_ORIGINS", DEFAULT_CORS_ORIGINS)
    return [origin.strip() for origin in raw.split(",") if origin.strip()]


def create_app() -> FastAPI:
    app = FastAPI(
        title="Aegis",
        version="0.0.0",
        docs_url="/docs",
        redoc_url=None,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_cors_origins(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def request_id_middleware(request: Request, call_next) -> Response:
        request_id = request.headers.get(REQUEST_ID_HEADER) or str(uuid.uuid4())
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers[REQUEST_ID_HEADER] = request_id
        return response

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app
