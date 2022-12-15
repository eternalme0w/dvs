from main import app
from website.models import List
from website import db


def test_post_task():
    client = app.test_client()
    client.post('/post_task', data = {"text": "PYTEST", "deadline": "00.00.00"})
    response = client.get('/todo')
    assert b'PYTESTik' and b"deadline" in response.data



