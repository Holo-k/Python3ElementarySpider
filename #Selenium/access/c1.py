from selenium import webdriver
from selenium.webdriver.edge.options import Options

# options = Options()
# options.add_argument("--headless")

browser = webdriver.Edge()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()
