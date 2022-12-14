from main import app

def test_delete_list():
    client = app.test_client()
    res = client.delete('/delete_task/22')
    json_res = res.get_json()
    print (json_res)
    assert res.status_code == 203
