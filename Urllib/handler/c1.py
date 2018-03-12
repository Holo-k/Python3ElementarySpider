from urllib import request

#设置代理,其余参看官方网站

proxy_handler = request.ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'http://127.0.0.1:9743'
})
opener = request.build_opener(proxy_handler)
response = opener.open('https://www.baidu.com')
print(response.read())