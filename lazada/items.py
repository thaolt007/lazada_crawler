# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class ProductItem(Item):
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

class CommentItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sku = Field()
    rating = Field()
    detail = Field()
    nickname = Field()
    id_rating_review = Field()
    fk_customer = Field()
    created_at = Field()
    title = Field()
    votes_up = Field()
    votes_down = Field()

