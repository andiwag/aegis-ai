"""FastAPI application factory."""

from __future__ import annotations

import uuid

from fastapi import FastAPI, Request
from starlette.responses import Response

REQUEST_ID_HEADER = "X-Request-ID"


def create_app() -> FastAPI:
    app = FastAPI(
        title="Aegis",
        version="0.0.0",
        docs_url="/docs",
        redoc_url=None,
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
