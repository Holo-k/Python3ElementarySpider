import requests

proxies = {
    'http': 'socks5://127.0.0.1:9743',
    'https': 'socks5://127.0.0.1"9743'
}

response = requests.get('https:www.taobao.com', proxies=proxies)
print(response.status_code)

#非http, https的代理  如:socks
#如果要使用socks
# pip3 install 'requests[socks]'