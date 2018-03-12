import requests

response = requests.get('http://www.baidu.com')
print(type(response))
print(response.status_code)
print(response.text)
print(response.cookies)