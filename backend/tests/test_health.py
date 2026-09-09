from aegis.api.app import REQUEST_ID_HEADER


def test_health_ok(client) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert REQUEST_ID_HEADER in response.headers


def test_health_echoes_request_id(client) -> None:
    response = client.get("/health", headers={REQUEST_ID_HEADER: "test-id-1"})
    assert response.headers[REQUEST_ID_HEADER] == "test-id-1"
