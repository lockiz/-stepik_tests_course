import json

data = '{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}'

print(type(json.loads(data)))