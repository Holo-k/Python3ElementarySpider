import requests

try:
    response = requests.get(
        'https://www.httpbin.org/get',
        timeout=0.2)  #若不能在0.1秒内应答，则抛出requests.exceptions.ConnectTimeout
    print(response.status_code)
except requests.exceptions.Timeout as e:
    print('TimeOut') 