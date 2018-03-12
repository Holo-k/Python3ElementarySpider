from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
browser = webdriver.Edge()
try:
    browser.get('http://www.bing.com')

except TimeoutException as e:
    print('Time out')
    print(e.msg)
try:
    browser.find_element(by=By.ID, value='hello')
except NoSuchElementException as e:
    print('No Found')
    print(e.msg)
else:
    browser.close()