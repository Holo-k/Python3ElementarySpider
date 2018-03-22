from pyspider.libs.base_handler import *
import pymongo


class Handler(BaseHandler):
    crawl_config = {}
    client = pymongo.MongoClient('localhost')
    db = client['TripAdvisor']

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl(
            'https://www.tripadvisor.cn/Attractions-g298564-Activities-Kyoto_Kyoto_Prefecture_Kinki.html',
            callback=self.index_page,
            validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('div.listing_title > a').items():
            self.crawl(
                each.attr.href, callback=self.detail_page, validate_cert=False)
        next = response.doc('.pagination >a.nav.next').attr.href
        self.crawl(next, callback=self.index_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        name = response.doc('h1').text()
        rating = response.doc('span.header_rating > div > a').text()
        info = response.doc(
            'div.section.location > div.detail_section.address').text()
        duration = response.doc(
            'div.section.hours > div > div:nth-child(2) > div').text()
        introduction = response.doc(
            'div.prw_rup.prw_common_location_description > div > div.text'
        ).text()
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            'name': name,
            'rating': rating,
            'info': info,
            'duration': duration,
            'introduction': introduction
        }

    def on_result(self, result):
        if result:
            self.save_to_mongo(result)

    def save_to_mongo(self, result):
        if self.db['TripAdvisor'].insert(result):
            print('保存成功')
