# socrata_crawl.py - crawlspider

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from socrata.items import SocrataItem

class MySpider(CrawlSpider):

	name = 'socrata2'
	allowed_domains = ['opendata.socrata.com']
	start_urls = [
		"https://opendata.socrata.com"
	]

	rules = (Rule
		(SgmlLinkExtractor(
			allow=("browse\?utf8=%E2%9C%93&page=\d*"),
			restrict_xpaths=('//a[@title="Next Page"]')
		),callback = "parse_items", follow= True),)

	def parse_items(self, response):
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