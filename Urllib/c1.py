from urllib import request, parse, error
import socket

response = request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))

##--------------------------------------------------------------

# #post
data = bytes(parse.urlencode({"name": "poi"}), encoding='utf-8')
response = request.urlopen(
    'http://httpbin.org/post', data=data)  #data keyword -> bytes
print(response.read())

##--------------------------------------------------------------

response = request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())

try:
    response = request.urlopen('http://httpbin.org/get', timeout=0.1)
except error.URLError as e:
    print(e.reason)  #-> class
    if isinstance(e.reason, socket.timeout):
        print('time out')  # -> time out

##--------------------------------------------------------------

response = request.urlopen('https://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

##--------------------------------------------------------------
