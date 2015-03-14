import requests
import json

apiKey = 'OOR23GuWwf'
payload = {'token':apiKey}
payload = json.dumps(payload)

r = requests.post('http://challenge.code2040.org/api/getstring',data=payload)
print json.loads(r.text)['result']

stringToReverse = json.loads(r.text)['result']
# stringToReverse = 'jason'
reversedString = ''
i = len(stringToReverse) - 1
while(i >= 0):
    reversedString = reversedString + stringToReverse[i]
    i -= 1

r = requests.post('http://challenge.code2040.org/api/validatestring',
                  json.dumps({"token": apiKey, "string": reversedString}))
print r.text


asdfkjsdf;lkasjdf;lk
