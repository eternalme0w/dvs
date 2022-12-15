from main import app


def test_post_task():
    client = app.test_client()
    client.post('/post_task', data = {"text": "PYTESTik", "deadline": "00.00.00"})
    response = client.get('/todo')
    assert b'PYTESTik' and b"00.00.00" in response.data



