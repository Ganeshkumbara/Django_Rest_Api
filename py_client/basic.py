import requests
import pprint
endpoint = "https://httpbin.org/anything"

get_res = requests.get(endpoint, json={'query':'tested123'})
pprint.pprint(get_res.json()) # Http request
print(get_res.status_code)