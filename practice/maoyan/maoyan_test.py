import requests
import re
from requests.exceptions import RequestException

root_pattern = re.compile('<dl class="board-wrapper">([\s\S]*?)</dl>', re.S)
index_pattern = re.compile('<i class="board-index board-index-\d+">(\d?)</i>',
                           re.S)
image_pattern = re.compile('<img data-src="([\s\S]*?)".*?class="board-img" />',
                           re.S)
title_pattern = re.compile(
    '<p class="name"><a.*?data-act="boarditem-click".*?>([\s\S]*?)</a></p>',
    re.S)
actor_pattern = re.compile('<p class="star">([\s\S]*?)</p>', re.S)
time_pattern = re.compile('<p class="releasetime">([\s\S]*?)</p>', re.S)
score_pattern = re.compile(
    '(?<=<p class="score"><i class="integer">)(\S*?)</i><i class="fraction">(\d?)</i></p>',
    re.S)


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
        "https": "36.6.159.31:61234",
        "https": "182.114.221.180:61202",
    }
    try:
        response = requests.get(url, headers=dict, proxies=proxies)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:

        return None


def parse_one_page(html):
    root_html = re.findall(root_pattern, html)
    items = []
    for item in root_html:
        temp = []
        index = re.findall(index_pattern, item)
        image = re.findall(image_pattern, item)
        title = re.findall(title_pattern, item)
        actor = re.findall(actor_pattern, item)
        time = re.findall(time_pattern, item)
        score = re.findall(score_pattern, item)
        yield {
            'index': index,
            'image': image,
            'title': title,
            'actor': actor,
            'time': time,
            'score': score
        }


def test(items):
    for item in items:
        for index in item['index']:
            

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    items=parse_one_page(html)
    test(items)



if __name__ == '__main__':
    main()