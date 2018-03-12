from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Edge()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('.ui-draggable')
target = browser.find_element_by_css_selector('.ui-droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
