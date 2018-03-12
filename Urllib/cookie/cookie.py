from urllib import request
import http.cookiejar

cookie = http.cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookiejar=cookie)
opener = request.build_opener(handler)
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(f'{item.name} =  {item.value}')
