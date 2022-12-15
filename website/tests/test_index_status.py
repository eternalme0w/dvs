from main import app

def test_index_status():
    client = app.test_client()
    res1= client.get('/')
    assert res1.status_code == 200
    res2 = client.get('/schedule/today')
    assert res2.status_code == 200
    res3 = client.get("/todo")
    assert res3.status_code == 200


