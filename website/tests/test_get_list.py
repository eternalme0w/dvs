from main import app

def test_get_list():
    client = app.test_client()
    res = client.get('/get_list')
    json_res = res.get_json()[0]
    assert json_res == ({'id': 1, 'text': 'laba', 'deadline': '20.12.2022', 'complete': True})
