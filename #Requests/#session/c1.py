import requests

requests.get('http://www.httpbin.org/cookies/set/name/poi')  #设置cookie
response = requests.get('http://www.httpbin.org/cookies')
print(response.text)


#注意，上面的两个request实际上是两个独立的存在，所以cookies为空