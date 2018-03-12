from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.get('https://www.taobao.com')
input_first = browser.find_element(by=By.ID, value='q')
print(input_first)
browser.close()
