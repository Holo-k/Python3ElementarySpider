import requests

response = requests.get('http://httpbin.org/get')
print(response.text)


data = {'name': 'poi', 'age': 21}
response = requests.get('http://httpbin.org/get', params=data)
print(response.text)