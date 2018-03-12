import requests
fro requests import urllib3
response = requests.get('http://www.dilidili.wang/', verify=False)  #对于没有https的链接，可以用verify=False来实现请求，不会像c1.py那样报错，但是仍会InsecureRequestWarning的警告
print(response.status_code)



#为了消除警告，请使用以下方法
urllib3.disable_warnings()
response = requests.get('http://www.dilidili.wang/', verify=False)  #对于没有https的链接，可以用verify=False来实现请求，不会像c1.py那样报错，但是仍会InsecureRequestWarning的警告
print(response.status_code)