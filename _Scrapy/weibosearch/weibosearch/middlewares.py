# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import requests
import json
from requests import ConnectionError
import logging
from scrapy.exceptions import IgnoreRequest


class CookiesMiddleware(object):
    def __init__(self, cookies_pool_url):
        self.cookies_pool_url = cookies_pool_url
        self.logging = logging.getLogger(__name__)

    def __get_random_cookies(self):
        try:
            response = requests.get(self.cookies_pool_url)
            if response.status_code == 200:
                return json.loads(response.text)
        except ConnectionError as e:
            return None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(cookies_pool_url=crawler.settings.get('COOKIES_POOL_URL'))

    def process_request(self, request, spider):
        cookies = self.__get_random_cookies()
        if cookies:
            request.cookies = cookies
            self.logging.debug('Using Cookies' + json.dumps(cookies))
        else:
            self.logging.debug('No Valid Cookies')

    def process_response(self, request, response, spider):
        if response.status in [300, 301, 302, 303]:
            try:
                redirect_url = response.headers['location']
                if 'passport' in redirect_url:
                    self.logging.warning('Need Login,Updating Cookies')
                elif 'weibo.cn/security' in redirect_url:
                    self.logging.warning('Account is Locked!')
                request.cookies = self.__get_random_cookies()
                return request
            except:
                raise IgnoreRequest
        elif response.status in [414]:
            return request
        else:
            return response
