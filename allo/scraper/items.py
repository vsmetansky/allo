"""Declares classes that represent extracted data.

Exported classes:
    StoreItem: A class that represents extracted item.
"""

import scrapy


class StoreItem(scrapy.Item):
    """Represents extracted item."""

    name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    info = scrapy.Field()
