import requests

from requests.exceptions import ReadTimeout, HTTPError, RequestException

try:
    response = requests.get('http://httpbin.org/get', timeout=0.5)
    print(response.status_code)
except ReadTimeout as e:
    print('TimeOut')
except HTTPError as e:
    print('Http errpr')
except RequestException as e:  #RequestException 为父类
    print('Error')