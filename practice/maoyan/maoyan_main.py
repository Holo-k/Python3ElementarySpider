import json
import requests
from requests.exceptions import RequestException
import re
import time
from multiprocessing import Pool


def get_one_page(url):

    dict = {
        'Accept':
        'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept':
        'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Language':
        'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
        'Connection':
        'Keep-Alive',
        'Cookie':
        '_csrf=7c2c5a63c28cfe64a6da59a3e97c55af133ecb6480d83485ec04b4ab6f031e1e; uuid=1A6E888B4A4B29B16FBA1299108DBE9C4FB33D70020EF46D4F050F872543DCCE; __mta=89095588.1520684242453.1520689451763.1520689831050.7; td_cookie=18446744071250743576; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_s=f170bee4e2261335ccad9f02f0f4%7C%7C13',
        'Host':
        'maoyan.com',
        'Referer':
        'http://maoyan.com/board',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    }

    proxies = {
        'https': '36.6.159.31:61234',
        'https': '182.114.221.180:61202',
    }

    try:
        response = requests.get(url, headers=dict, proxies=proxies)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a' +
        '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>' +
        '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])
    # for i in range(10):
    #     main(offset=i * 10)
    #     time.sleep(1)