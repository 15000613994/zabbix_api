import requests
import json



url = "https://ipamtool.yfai.com/api/ipamYfai"

request_ipam = requests.request('GET', url, headers=headers, data=json.dumps(data),)