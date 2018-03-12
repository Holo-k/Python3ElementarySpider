import requests

file = {'file1': open('cookie_lwp.txt', mode='r')}
response = requests.post('http://www.httpbin.org/post', files=file)
print(response.text)

file = {'file1': open('01.jpg', mode='rb')}  # 二进制文件 上传 mode='rb' 否则错误
response = requests.post('http://www.httpbin.org/post', files=file)
print(response.text)