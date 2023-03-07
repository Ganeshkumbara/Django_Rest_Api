import requests
import pprint
endpoint = 'http://localhost:8080/api/'

get_res = requests.get(endpoint, json={'query':'tested123'}, params={'passing':123})
# print(get_res.text)
print(get_res.status_code)
print(get_res.json())