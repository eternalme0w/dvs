from main import app

def test_get_list():
    client = app.test_client()
    res = client.get('/todo')
    assert bytes('ПОЧИСТИТЬ ЗУБЫ', 'utf-8') in res.data
