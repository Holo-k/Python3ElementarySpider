'''
find()的查找范围是节点的所有子孙节点，而如果我们只想查找子节点，那么可以用children()方法：
'''

from pyquery import PyQuery

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = PyQuery(html)
items = doc('.list')
print(items.children('.active'))  #查找子节点，那么可以用children()方法