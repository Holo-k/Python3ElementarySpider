import urllib.request as request, http.cookiejar as cookiejar

cookie = cookiejar.LWPCookieJar()
cookie.load(
    filename='cookie_lwp.txt', ignore_discard=True, ignore_expires=True)
handler = request.HTTPCookieProcessor(cookiejar=cookie)
opener = request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))