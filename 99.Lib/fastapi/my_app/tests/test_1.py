from fastapi.testclient import TestClient
from my_app.helper import other_server
from my_app.main import app, common_parameters

cli = TestClient(app)


"""
The app.dependency_overrides API is meant to override dependencies provided by "Depends",
it's NOT an API to mock module variables used in your FastAPI app.
To be able to use app.dependency_overrides, provide your dependencies via "Depends" API.
"""


def override_common_params():
    return {"q": "Good job", "skip": 111, "limit": 222}


app.dependency_overrides[common_parameters] = override_common_params


########################################################################################
def test_read_items():
    resp = cli.get("/items?q=hello world&skip=123&limit=456")
    resp_obj = resp.json()
    assert resp_obj["q"] == "Good job"
    assert resp_obj["skip"] == 111
    assert resp_obj["limit"] == 222


def test_read_users():
    resp_obj = cli.get("/users/1").json()
    assert resp_obj["is_admin"] == True

    resp_obj = cli.get("/users/2").json()
    assert resp_obj["is_admin"] == False
