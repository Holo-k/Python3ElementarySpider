import re
import requests

url = 'https://book.douban.com/'
content = requests.get(url).text
pattern = re.compile(
    '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',
    flags=re.S)
results = re.findall(pattern, content)
print(results)
