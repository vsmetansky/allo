import scrapy


class StoreItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    info = scrapy.Field()
