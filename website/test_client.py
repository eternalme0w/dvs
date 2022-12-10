import requests

BASE = "http://127.0.0.1:5004"

response = requests.put(BASE + '/put_complete/1', json={"complete": True})
print(response.json())
