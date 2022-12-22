from main import app

def test_index_status():
    client = app.test_client()
    client.post('/', data={"group": "1307", "password": "1307"})
    res1 = client.get('/main', follow_redirects=True)
    assert res1.status_code == 200
    res2 = client.get('/schedule/today', follow_redirects=True)
    assert res2.status_code == 200
    res3 = client.get("/todo", follow_redirects=True)
    assert res3.status_code == 200



