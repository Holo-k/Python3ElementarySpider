from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.get('https://www.taobao.com')
lis = browser.find_elements(by=By.CSS_SELECTOR, value='.service-bd li')
print(type(lis))
print(type(lis[0]))
print(lis)
browser.close()