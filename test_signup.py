import urllib.request
import json

req = urllib.request.Request(
    'http://localhost:8000/auth/signup',
    data=json.dumps({"username":"testuser","email":"test@test.com","password":"password123","role":"accountant"}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    with urllib.request.urlopen(req) as response:
        print(response.status)
        print(response.read().decode())
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read().decode())
