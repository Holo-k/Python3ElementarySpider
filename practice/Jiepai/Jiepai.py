import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re
from config import *
import pymongo
import os
from hashlib import md5
from multiprocessing import Pool
from json.decoder import JSONDecodeError

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]


def get_page_index(offset, keyword):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print('请求出错啦ε=ε=ε=(~￣▽￣)~')
        return None


def parse_page_index(htmls):
    try:
        data = json.loads(htmls)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError as e:
        pass


def get_page_detail(url):
    headers = {
        'Accept':
        'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding':
        'gzip, deflate, br',
        'Accept-Language':
        'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
        'Cookie':
        'tt_webid=6531587635668289038; WEATHER_CITY=%E5%8C%97%E4%BA%AC; CNZZDATA1259612802=241428750-1520751739-https%253A%252F%252Fwww.bing.com%252F%7C1520767936; tt_webid=6531587635668289038; __tasessionId=ifyho7mod1520768267688; uuid=w:113bfef04d5a45e18f15a3aa957db2f3; UM_distinctid=1621407ee0873c-0db73e7c27d625-7047503f-144000-1621407ee09978; tt_webid=6531587635668289038',
        'Host':
        'www.toutiao.com',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print('请求出错啦ε=ε=ε=(~￣▽￣)~')
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, features='lxml')
    title = soup.find(name='title').get_text()
    articleInfo_pattern = re.compile('content:.*?([\s\S]*?)', flags=re.S)
    images_pattern = re.compile('', flags=re.S)
    result = re.search(articleInfo_pattern, html)
    if result:
        data = json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            [download_image(url_image) for url_image in images]
            return {'title': title, 'url': url, 'images': images}
    else:
        print('poi')


def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MongoDB成功', result)
        return True
    return False


def download_image(url):
    print('当前正在下载: ', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException as e:
        print('请求出错啦ε=ε=ε=(~￣▽￣)~', url)
        return None


def save_image(content):
    # file_path=f'{os.getcwd()}/{md5(content).hexdigest()}.jpg'
    file_path = '{0}/{1}.{2}'.format(os.getcwd(),
                                     md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, mode='wb') as file:
            file.write(content)


def main(offset):
    htmls = get_page_index(offset, KEYWORD)
    article_url = parse_page_index(htmls)
    for url in article_url:
        if url:
            detail_html = get_page_detail(url)
            if detail_html:
                result = parse_page_detail(detail_html, url)
                if result:
                    save_to_mongo(result)


if __name__ == '__main__':
    pool = Pool()
    groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
    pool.map(main, groups)
