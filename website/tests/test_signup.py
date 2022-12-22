from main import app


def test_signup():
    client = app.test_client()
    client.post('/signup', data={"group": "0309", "password": "0309"})
    client.post('/',data={"group": "0309", "password": "0309"})
    res = client.get('/main', follow_redirects=True)
    assert res.status_code == 200

9
