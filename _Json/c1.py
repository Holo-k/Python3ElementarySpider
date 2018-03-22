import requests
import json

url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start=0'
response = requests.get(url, stream=True)

# with open('tv.txt', mode='wb') as file:
#     for content in response.iter_content(chunk_size=32):
#         file.write(content)

with open('tv2.txt', mode='w', encoding='utf-8') as file:
    file.write(json.dumps(response.json(), ensure_ascii=False, indent=2))
'''
ensure_ascii:让文字现实为本来的意思
indent：让下一行在上一行的基础上空格
'''