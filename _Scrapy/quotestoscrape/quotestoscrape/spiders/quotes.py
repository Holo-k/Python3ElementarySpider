# -*- coding: utf-8 -*-
import scrapy
from quotestoscrape.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']
    custom_settings = {   #覆盖全局的配置信息，settings.py
        'DEFAULT_REQUEST_HEADERS': {
            'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':
            'en',
        }
    }

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuotesItem()
            text = quote.css('.pager .next a::attr(href)').extract_first()
            author = quote.css('.author::text').extract_first()
            tages = quote.css('.tags .tag::text').extract()
            item['text'] = text
            item['author'] = author
            item['tags'] = tages
            print(type(item))
            yield item
        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        print('-------------------------------')
        yield scrapy.Request(url=url, callback=self.parse)
