import requests

_URL = 'http://admin:admin@192.168.178.48:8080/me/configure'

req = requests.Request('GET', _URL)
print(req.data)
