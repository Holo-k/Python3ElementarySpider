from pyquery import PyQuery

html = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''

doc = PyQuery(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'poi')
# li.attr('name', 'poi', 'age', '21') #错误
print(li)
li.text('poi  poi')  #会完全替换之前的文本
li.append('poi   poi')
print(li)
li.html('<span><font color="red">Poi</font></span>')
print(li)
