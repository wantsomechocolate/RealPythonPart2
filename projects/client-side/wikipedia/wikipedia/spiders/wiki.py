from scrapy.spider import Spider
from scrapy.selector import Selector

from wikipedia.items import WikipediaItem
from urlparse import urljoin

class WikipediaSpider(Spider):

	#name the spider
	name = 'wiki'

	#allowed domains to scrape
	allowed_domains = ["en.wikipedia.org/"]

	#urls the spider beings to crawl from
	start_urls = ["http://en.wikipedia.org/wiki/Category:2014_films"]

	#parses and returns the scraped data
	def parse(self, response):
		hxs = Selector(response)
		titles = hxs.xpath('//tr[@style="vertical-align: top;"]//li')
		base_url = "http://en.wikipedia.org"
		items=[]
		for title in titles:
			item = WikipediaItem()
			intra_url = title.xpath("a/@href").extract()
			item["movie_title"] = title.xpath("a/text()").extract()
			item["movie_url"] = urljoin(base_url,intra_url[0])
			items.append(item)
		return items
		#return "test"