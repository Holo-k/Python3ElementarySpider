from selenium import webdriver
import time
browser = webdriver.Edge()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')

browser.back()
time.sleep(1)
browser.forward()
