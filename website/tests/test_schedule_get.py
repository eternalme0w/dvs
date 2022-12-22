from main import app

def test_schedule_get():
    client = app.test_client()
    client.post('/',data={"group": "1307", "password": "1307"})
    response = client.get('/schedule/date/23/12/2022')
    assert bytes("Теоретические основы электротехники", 'utf-8') in response.data


