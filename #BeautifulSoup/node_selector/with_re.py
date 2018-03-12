import multiprocessing as mp
import re
import time
from bs4 import BeautifulSoup
from urllib import request
import requests

base_url = 'https://morvanzhou.github.io/'


def crawl(url):
    response = request.urlopen(url).read().decode()
    return response


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([request.urljoin(base_url, url['href']) for url in urls])
    url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url


def multiprocessing():
    unseen = set([
        base_url,
    ])
    seen = set()

    if base_url != 'http://127.0.0.1:4000/':
        restricted_crawl = True
    else:
        restricted_crawl = False
    pool = mp.Pool(4)
    count, t1 = 1, time.time()

    while len(unseen) != 0:
        if restricted_crawl and len(seen) > 20:
            break
        print('\nDistributed Crawling...')
        crawl_job = [pool.apply_async(crawl, args=(url, )) for url in unseen]
        htmls = [html.get() for html in crawl_job]
        htmls = [html for html in htmls if html is not None]
        print('\nDistributed Parsing...')

        parse_job = [pool.apply_async(parse, args=(html, )) for html in htmls]
        results = [result.get() for result in parse_job]

        print('\nAnalysing...')

        seen.update(unseen)
        unseen.clear()

        for title, page_urls, url in results:
            print(count, title, url)
            count += 1
            unseen.update(page_urls - seen)
    print(f'Total time: {time.time() - t1} s')


def normal():
    unseen = set([
        base_url,
    ])
    seen = set()

    if base_url != 'http://127.0.0.1:4000/':
        restricted_crawl = True
    else:
        restricted_crawl = False
    count, t1 = 1, time.time()

    while len(unseen) != 0:
        if restricted_crawl and len(seen) > 20:
            break
        print('\nDistributed Crawling...')
        htmls = [crawl(url) for url in unseen]
        print('\nDistributed Parsing...')

        results = [parse(html) for html in htmls]

        print('\nAnalysing...')

        seen.update(unseen)
        unseen.clear()

        for title, page_urls, url in results:
            print(count, title, url)
            count += 1
            unseen.update(page_urls - seen)
    print(f'Total time: {time.time() - t1} s')


if __name__ == '__main__':
    # base_url = 'https://morvanzhou.github.io/'
    multiprocessing()
    normal()