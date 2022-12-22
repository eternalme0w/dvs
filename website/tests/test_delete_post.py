from main import app
from website.models import List

def test_delete_list():
    client = app.test_client()

    with app.app_context():
        del_task = List.query.filter_by(id=4).first()
        assert del_task != None

    client.post('/', data={"group": "1307", "password": "1307"})

    client.post('/del_task', data={'id':'4'})
    res = client.get('/todo',follow_redirects=True)
    assert res.status_code == 200

    with app.app_context():
        del_task = List.query.filter_by(id=4).first()
        assert del_task == None

