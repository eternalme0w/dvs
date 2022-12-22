from main import app


def test_post_task():
    client = app.test_client()
    res_log = client.post('/', data={"group": "1307", "password": "1307"})
    res = client.post('/post_task', data = {"text": "PYTEST", "deadline": "00.00.00"})
    response = client.get('/todo', follow_redirects=True)
    assert b'PYTEST' and b"00.00.00" in response.data



