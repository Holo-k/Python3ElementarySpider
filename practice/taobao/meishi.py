from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import re
from pyquery import PyQuery as pq
import pymongo
from config import *
chrome_options = Options()
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--test-type")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--ignore-certificate-errors")
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def search():
    try:
        browser.get('https://www.taobao.com')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '#J_TSearchForm > div.search-button > button')))
        input.send_keys('Lumia 950xl')
        submit.click()
        total = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 '#mainsrp-pager > div > div > div > div.total')))
        get_product()
        return total.text
    except TimeoutError as e:
        return search()


def next_page(page_num):
    try:
        input = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '#mainsrp-pager > div > div > div > div.form > input')))
        input.clear()
        input.send_keys(page_num)
        submit = wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'
            )))
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,
                '#mainsrp-pager > div > div > div > ul > li.item.active > span'
            ), str(page_num)))
        get_product()
    except TimeoutError as e:
        return next_page(page_num)


def get_product():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('保存MongoDB成功', result)
    except Exception as e:
        print('保存失败')


def main():
    try:
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))
        for page_num in range(2, total + 1):
            next_page(page_num)
    except Exception as e:
        print('出错啦')
    finally:
        browser.close()


if __name__ == '__main__':
    main()
