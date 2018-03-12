import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}
response = requests.get('https://www.zhihu.com/explore', headers=headers)  #不添加headers 不能请求信息
print(response.text)