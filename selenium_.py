from selenium import webdriver
from selenium.webdriver.chrome.options import Options


driver = webdriver.Edge()
driver.get('https://h.bilibili.com/d')
print(driver.page_source)
