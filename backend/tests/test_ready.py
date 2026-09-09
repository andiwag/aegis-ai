from fastapi.testclient import TestClient

from aegis.api.app import create_app


def test_ready_ok_when_database_answers(monkeypatch) -> None:
    monkeypatch.setattr("aegis.api.app.check_connection", lambda engine: None)
    client = TestClient(create_app())
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready_unavailable_when_database_fails(monkeypatch) -> None:
    def fail(engine) -> None:
        raise OSError("connection refused")

    monkeypatch.setattr("aegis.api.app.check_connection", fail)
    client = TestClient(create_app())
    response = client.get("/ready")
    assert response.status_code == 503
    assert response.json() == {"status": "unavailable"}


def test_health_ok_when_database_fails(monkeypatch) -> None:
    def fail(engine) -> None:
        raise OSError("connection refused")

    monkeypatch.setattr("aegis.api.app.check_connection", fail)
    client = TestClient(create_app())
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
