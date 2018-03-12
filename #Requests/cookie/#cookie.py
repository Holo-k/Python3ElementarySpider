import requests

response = requests.get('https://www.baidu.com')
cookies = response.cookies

for k,v in cookies.items():
    print(f'{k} = {v}')
