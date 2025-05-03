from fastapi.testclient import TestClient
from my_app.main import app

cli = TestClient(app)

def test_read_items():
    resp = cli.get('/items?q=hello world&skip=123&limit=456')
    resp_obj = resp.json()
    assert resp_obj['q'] == "hello world"
    assert resp_obj['skip'] == 123
    assert resp_obj['limit'] == 456
