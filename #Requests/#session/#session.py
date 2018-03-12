import requests

session = requests.Session()
session.get('http://www.httpbin.org/cookies/set/name/poi')  #设置cookie
response = session.get('http://www.httpbin.org/cookies')
print(response.text)