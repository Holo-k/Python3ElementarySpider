from pyquery import PyQuery as pq

doc = pq(filename='./demo.html')
print(type(doc('li')))  #<class 'pyquery.pyquery.PyQuery'>
print(doc('li.item-1').text())
print(doc('li.item-1').find('a').text())
