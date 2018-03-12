import urllib.request as request, urllib.error as weberror

try:
    response = request.urlopen('http://www.sdafkla.com')
except weberror.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except weberror.URLError as e: # URLError -> HTTPError(sub)
    print(e.reason)
else:
    print('Request Successfully')