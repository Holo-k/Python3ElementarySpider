from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())  #标准式格式化标签文本，包括补全标签,缩进格式输出等
print(soup.title.get_text())  #获取titile的文本
# print(soup.title.string) #获取titile的文本
print(type(soup.title))  #<class 'bs4.element.Tag'>


print(soup.head)
print(soup.p)

print(soup.title.name) #获取名称



#获取属性
print(soup.p.attrs)
print(soup.p.attrs['name'])

print(soup.p['name'])
print(soup.p['class'])