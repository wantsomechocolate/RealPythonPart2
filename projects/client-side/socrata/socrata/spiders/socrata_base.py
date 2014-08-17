# socrata_base.py - basespider

from scrapy.spider import Spider
from scrapy.selector import Selector

from socrata.items import SocrataItem

class MySpider(Spider):
	name = 'socrata'
	allowed_domains = ['opendata.socrata.com']
	start_urls = [
		"https://opendata.socrata.com"
	]

	def parse(self, response):
		hxs = Selector(response)
		titles = hxs.xpath('//tr[@itemscope="itemscope"]')
		items = []

		for t in titles:
			item = SocrataItem()
			item['text'] = t.xpath('td[2]/div/span/text()').extract()
			item['url'] = t.xpath('td[2]/div/a/@href').extract()
			item['views'] = t.xpath('td[3]/span/text()').extract()
			items.append(item)

		return(items)