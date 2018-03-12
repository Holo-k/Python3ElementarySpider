import urllib.request as request, urllib.error as error
import socket

try:
    response = request.urlopen('http://httpbin.org/get', timeout=0.1)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('time out')
else:
    print('Request Successfully')