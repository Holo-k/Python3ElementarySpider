import requests

respone = requests.get('http://www.jianshu.com')
print(type(respone.status_code), respone.status_code)

exit() if not respone.status_code == 200 else print('Request Successfully')

exit() if not respone.status_code == requests.codes.ok else print(
    'Request Successfully')
