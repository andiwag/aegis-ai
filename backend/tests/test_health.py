from aegis.api.app import REQUEST_ID_HEADER


def test_health_ok(client) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert REQUEST_ID_HEADER in response.headers


def test_health_echoes_request_id(client) -> None:
    response = client.get("/health", headers={REQUEST_ID_HEADER: "test-id-1"})
    assert response.headers[REQUEST_ID_HEADER] == "test-id-1"


def test_cors_allows_vite_origin(client) -> None:
    response = client.get(
        "/health",
        headers={"Origin": "http://127.0.0.1:5173"},
    )
    assert response.headers["access-control-allow-origin"] == "http://127.0.0.1:5173"
