import urllib.request as request, urllib.parse as parse

data = bytes(parse.urlencode({"name": "poi"}), encoding='utf-8')
response = request.urlopen(
    'http://httpbin.org/post', data=data)  #data keyword -> bytes
print(response.read())