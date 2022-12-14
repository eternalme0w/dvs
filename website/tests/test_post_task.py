from main import app
from website.models import List
from website import db


def test_post_task():
    client = app.test_client()
    data = {"text": "TESTTESTTEST", "deadline": "TEST_DATE"}
    task = List(text=data["text"], deadline=data["deadline"])
    with app.app_context():
        db.session.add(task)
        db.session.commit()
    response = client.post('/post_task')
    res = client.get('/get_list')
    json_res = res.get_json()[-1]
    print(json_res)



