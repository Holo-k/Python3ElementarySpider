import requests
import json

response = requests.get('http://www.httpbin.org/get')
print(type(response.json()))
data = response.json()
data2 = json.loads(response.text)
print(data)
print('-----------------------------------------')
print(data2)

print(data['headers'])