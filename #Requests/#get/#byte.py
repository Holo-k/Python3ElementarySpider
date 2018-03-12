import requests

response = requests.get(
    'https://images.dmzj.com/resource/news/2018/03/06/1520303703544173.jpg')
print(type(response.text))
print(type(response.content))
print(response.content)

with open('1.png', mode='wb') as file:
    for content in response.iter_content(chunk_size=32):
        file.write(content)