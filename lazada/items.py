# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class LazadaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    price_final = Field()
    price_old = Field()
    discount = Field()
    description = Field()
    image_url = Field()
    link_product = Field()
    date = Field()

    image = Field()
    sku = Field()

    comment = Field()

