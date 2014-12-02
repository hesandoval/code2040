import requests
import json

payload = {'email': 'hsandoval@csumb.edu', 'github': 'https://github.com/hesandoval/code2040.git'}
payload = json.dumps(payload)
print payload
r = requests.post('http://challenge.code2040.org/api/register', data=payload)

print r.text
