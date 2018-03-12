import urllib.request as request, urllib.error as weberror

try:
    response = request.urlopen('http://www.cs00jdasdil.com')
except weberror.URLError as e:
    print(e.reason)