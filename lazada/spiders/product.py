# -*- coding: utf-8 -*-
import scrapy
from lazada.items import ProductItem
import urlparse
import datetime
from scrapy.http import Request

class BasicSpider(scrapy.Spider):
	name = 'product'
	allowed_domains = ['web']
	start_urls = ['https://www.lazada.vn/dien-thoai-di-dong/?page=1']
	

	def parse(self, response):
		products = response.css('div.c-product-list > div.c-product-card')
		
		for product in products:
			item = ProductItem()

			sku = product.css('::attr(data-sku-simple)').extract()[0]
			item['sku'] = sku[:len(sku)-8]

			name = product.css('div.c-product-card__description > a::text').extract()[0]
			item['name'] = name.strip()

			url = product.css('div.c-product-card__img-placeholder >a::attr(href)').extract()[0]
			item['link_product'] = urlparse.urljoin(response.url,url)

			item['price_final'] = product.css('div.c-product-card__price-block > div '
				'> div > div > span.c-product-card__price-final::text').re('[.0-9]+')[0]

			try:
				item['discount'] = product.css(
					'div.c-product-card__price-block > div > div > div > '
					'span.c-product-card__discount::text').re('[.0-9]+')[0]
			except:
				item['discount'] = 0

			try:
				item['price_old'] =  product.css(
					'div.c-product-card__price-block > div > div > div '
					'> div.c-product-card__old-price::text').re('[.0-9]+')[0]
			except:
				item['price_old'] = item['price_final']
				
			#item['date'] = datetime.datetime.now()
			
			yield item

		next_page = response.css('div.c-paging > div.c-paging__wrapper > a.c-paging__next-link::attr(href)').extract()[0]
		if next_page is not None:
			yield Request(next_page, callback=self.parse, dont_filter=True)

		