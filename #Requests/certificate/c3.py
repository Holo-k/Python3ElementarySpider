import requests

response = requests.get(
    'http://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)  #假设本地存在一个这样的符合要求的证书就行