from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Edge()
browser.get(
    'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to_frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException as e:
    print(e.msg)
    print('NO Logo')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo.text)
browser.close()