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
items = doc('.list').parent()  #该节点的直接父节点，也就是说，它不会再去查找父节点的父节点，即祖先节点。
print(items)  #输出包括父节点
print(items.html())  #输出不包括父节点  ->str