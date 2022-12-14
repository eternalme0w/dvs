from main import app

def test_index_status():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

