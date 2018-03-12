from pyquery import PyQuery

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

doc = PyQuery(html)

a = doc('a')
print(a, type(a))
print(a.attr('href'))  #当返回结果包含多个节点时，调用attr()方法，只会得到第一个节点的属性
print(a.attr.href)

print(doc('li.item-0.active')('a').attr('href'))
print('-----------------------------------------------------')

for item in doc('li').items():
    print(item.find('a').attr('href'))