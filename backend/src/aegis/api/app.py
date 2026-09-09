"""FastAPI application factory."""

from __future__ import annotations

import uuid

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.responses import Response

from aegis.db import check_connection, create_db_engine, create_session_factory
from aegis.settings import get_settings

REQUEST_ID_HEADER = "X-Request-ID"


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title="Aegis",
        version="0.0.0",
        docs_url="/docs",
        redoc_url=None,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.state.engine = create_db_engine(settings.database_url)
    app.state.SessionLocal = create_session_factory(app.state.engine)

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

    @app.get("/ready")
    def ready(request: Request) -> JSONResponse:
        try:
            check_connection(request.app.state.engine)
        except Exception:
            return JSONResponse({"status": "unavailable"}, status_code=503)
        return JSONResponse({"status": "ok"})

    return app
