import requests
import json

payload = {'email': 'hsandoval@csumb.edu', 'github': 'https://github.com/hesandoval/code2040'}
payload = json.dumps(payload)
print payload
r = requests.post('http://challenge.code2040.org/api/register', params=payload)

print r.text
