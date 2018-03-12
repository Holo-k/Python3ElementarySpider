import requests
from requests.auth import HTTPBasicAuth

response = requests.get(
    'http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
print(response.status_code)

response = requests.get('http://120.27.34.24:9001/', auth=('user', '123'))
print(response.status_code)

#以上两种方式均可
