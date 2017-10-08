# -*- coding: utf-8 -*-
import scrapy
from lazada.items import LazadaItem
import urlparse
import datetime
from scrapy.http import Request

class BasicSpider(scrapy.Spider):
	name = 'comment'
	allowed_domains = ['web']
	start_urls = ['https://www.lazada.vn/dien-thoai-di-dong/?page=1']

	def parse(self, response):
		products = response.css('div.c-product-list > div.c-product-card')
		
		for product in products:
			item = LazadaItem()
			sku = product.css('::attr(data-sku-simple)').extract()[0]
			item['sku'] = sku[:len(sku)-8]


		next_page = response.css('div.c-paging > div.c-paging__wrapper > a.c-paging__next-link::attr(href)').extract()[0]
		if next_page is not None:
			yield Request(next_page, callback=self.parse, dont_filter=True)

	def genlink(page, sku):
		link = 'http://www.lazada.vn/ajax/ratingreview/reviewspage?page='
		link = link + str(page) + '&sort=relevance&sortDirection=desc&sku=' + sku
		return link