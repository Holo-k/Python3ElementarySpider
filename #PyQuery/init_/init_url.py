from pyquery import PyQuery as pq

doc = pq(url='http://www.dilidili.wang', encoding='utf-8')
print(doc('title').html())