from main import app

def test_schedule_get():
    client = app.test_client()
    response = client.get('/schedule/date/16/12/2022')
    assert bytes("Теоретические основы электротехники", 'utf-8') in response.data


