import urllib.request as request, urllib.parse as parse

result = parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
print(result.hostname)

result = parse.urlparse(
    'www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(f'\n{result}')

result = parse.urlparse(
    'http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(f'\n{result}')

result = parse.urlparse(
    'http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(f'\n{result}')

result = parse.urlparse(
    'http://www.baidu.com/index.html#comment', allow_fragments=False)
print(f'\n{result}')

data = [
    'http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment'
]
print(parse.urlunparse(data))
