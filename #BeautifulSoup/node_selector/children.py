from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html, features='lxml')
# print(soup.p.contents)  #这种方式也可以，但我个人认为用下面的这种方式更好

print(soup.p.children)  #<list_iterator object

print(type(soup.p.children))
for i, child in enumerate(soup.p.children):
    print(i, child)
