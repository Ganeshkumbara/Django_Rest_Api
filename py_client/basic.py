import requests
import pprint
endpoint = 'http://localhost:8080/'

get_res = requests.get(endpoint, json={'query':'tested123'})
print(get_res.text)
