# -*- coding: utf-8 -*-
import scrapy
from lazada.items import CommentItem
import urlparse
import datetime
from scrapy.http import Request
import json

def genlink(page, sku):
		link = 'http://www.lazada.vn/ajax/ratingreview/reviewspage?page='
		link = link + str(page) + '&sku=' + sku
		return link

class BasicSpider(scrapy.Spider):
	name = 'comment'
	allowed_domains = ['lazada.vn']
	start_urls = ['https://www.lazada.vn/dien-thoai-di-dong/?page=1']

	

	def parse(self, response):
		products = response.css('div.c-product-list > div.c-product-card')
		# self.log(products[0])
		for product in products[:1]:
			simple_sku = product.css('::attr(data-sku-simple)').extract()[0]
			sku = simple_sku[:len(simple_sku)-8]
			link = genlink(page=1,sku=sku)
			yield Request(link, #meta={
				dont_filter=True,
				#'dont_redirect':True,
				#'handle_httpstatus_list': [302]}, 
				callback=self.parse_comment)

		# next_page = response.css('div.c-paging > div.c-paging__wrapper > a.c-paging__next-link::attr(href)').extract()[0]
		# if next_page is not None:
		# 	yield Request(next_page, callback=self.parse, meta={'dont_filter'=True, 'dont_redirect'=True})
	def parse_comment(self, response):
		item = CommentItem()
		object = json.loads(response.body_as_unicode())
		number_comment = (object['data']['pagingHeadline']).split()[-1]
		self.log(number_comment)
		return

	