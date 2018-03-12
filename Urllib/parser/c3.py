import urllib.request as request, urllib.parse as parse

print(parse.urljoin('http://www.baidu.com', 'FAQ.html'))
print(parse.urljoin('http://www.baidu.com', 'https://bing.com'))
print(parse.urljoin('http://www.baidu.com', '?category=2#comment'))
print(parse.urljoin('http://www.baidu.com#comment', '?category=2'))

params = {'name': 'germey', 'age': 21}
base_url = 'http://www.baidu.com?'
url = base_url + parse.urlencode(params)
print(url)
