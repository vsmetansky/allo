from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

from scraper.items import StoreItem


class StoreItemSpider(CrawlSpider):
    name = 'store_item_spider'
    allowed_domains = ('allo.ua',)
    start_urls = ('https://allo.ua',)
    rules = (
        Rule(LinkExtractor(allow=(r'/ua/products/\w+?/$',))),
        Rule(LinkExtractor(
            allow=(r'/[-\w]+?[.]html$',)), callback='parse_item')
    )

    def __init__(self, item_num, *args, **kwargs):
        self.extracted_num = 0
        self.item_num = item_num
        super().__init__(*args, **kwargs)

    def count_items(self):
        if self.extracted_num < self.item_num:
            self.extracted_num += 1
        else:
            raise CloseSpider('Extracted all the items!')

    def parse_item(self, response):
        self.count_items()
        return StoreItem(
            name=self._get_name(response),
            price=self._get_price(response),
            image=self._get_image(response),
            info=self._get_info(response))

    def _get_name(self, response):
        return response.xpath('//h1[@id="product-title-h1"]/text()').get().strip()

    def _get_price(self, response):
        return response.xpath('//span[@class="price"]/text()').get().strip()

    def _get_image(self, response):
        return response.xpath('//img[@id="image"]/@src').get()

    def _get_info(self, response):
        paragraphs = response.xpath('//div[@class="cont"]/text()').getall()
        return ''.join(paragraphs).strip()
