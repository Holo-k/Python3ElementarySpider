from bs4 import BeautifulSoup
import re
html = '''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('link')))  #text参数可用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象，推荐使用re