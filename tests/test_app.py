"""
Tests pytest (unitaires) pour l'API.

On teste:
- GET / retourne 200
- GET /health retourne 200 si la DB répond (on mock la DB)
"""

from unittest.mock import patch
from api.app import create_app


def test_index_ok():
    app = create_app()
    client = app.test_client()

    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "API is running"


def test_health_ok_with_mocked_db():
    app = create_app()
    client = app.test_client()

    # On mock get_db_connection pour simuler une DB OK
    fake_conn = type("C", (), {})()
    fake_cur = type("Cur", (), {})()

    fake_cur.execute = lambda *_: None
    fake_cur.fetchone = lambda: (1,)
    fake_cur.close = lambda: None
    fake_conn.cursor = lambda: fake_cur
    fake_conn.close = lambda: None

    with patch("api.app.get_db_connection", return_value=fake_conn):
        res = client.get("/health")
        assert res.status_code == 200
        assert res.get_json()["status"] == "ok"
