import requests

data = {'name': 'poi', 'age': 21}
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}
response = requests.post('http://httpbin.org/post', data=data, headers=headers)
print(response.text)
print('-------------------------------------------------')
print(response.json())
