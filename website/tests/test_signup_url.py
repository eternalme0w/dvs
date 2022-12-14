from flask_login import current_user

from main import app


def test_sugnup_existing_user():
    client = app.test_client()
    group = "pytest6"
    password = "pytest6"

    res = client.post("/signup", data={
        "group": "pytestWORK+login7",
        "password": "pytest6"
    }, follow_redirects=True)

    assert b"Email address already exists." in res.data





