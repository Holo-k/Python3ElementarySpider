import requests

proxies = {'http': 'http://user:password@127.0.0.1:9743/'}
response = requests.get('https://www.taobao.com', proxies=proxies)  #假设你的代理需要用户名与密码
print(response.status_code)