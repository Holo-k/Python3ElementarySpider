import requests

repsonse = requests.get('http://www.dilidili.wang/')
print(repsonse.status_code)  #没有https 会抛出requests.exceptions.SSLError的错误