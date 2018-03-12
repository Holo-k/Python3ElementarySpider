import urllib.request as request, http.cookiejar as cookiejar

filename = './cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename=filename)
handler = request.HTTPCookieProcessor(cookiejar=cookie)
opener = request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
