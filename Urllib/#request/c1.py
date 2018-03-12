import urllib.request as webrequest, urllib.parse as parse

url = 'http://httpbin.org/post'
headers = {
    'User_Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
    'Host': 'httpbin.org'
}
dict = {'name': 'poi'}
data = bytes(parse.urlencode(dict), encoding='utf-8')
request = webrequest.Request(url, data=data, headers=headers, method='POST')
response = webrequest.urlopen(request)
print(response.read().decode('utf-8'))
