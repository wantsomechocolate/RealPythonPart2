from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from hackernews.items import HackernewsItem

class MySpider(BaseSpider):

	#name the spider
	name = 'hackernews'

	#allowed domains to scrape
	allowed_domains = ["news.ycombinator.com/"]
	#allowed_domains = ["3musesglass.com"]

	#urls the spider beings to crawl from
	start_urls = ["https://news.ycombinator.com/"]
	#start_urls = ["http://www.3musesglass.com/categories"]

	#parses and returns the scraped data
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select('//td[@class="title"]')
		items=[]
		for title in titles:
			item = HackernewsItem()
			item["title"] = title.select("a/text()").extract()
			item["url"] = title.select("a/@href").extract()
			items.append(item)

		return items

	# def parse(self, response):
	# 	hxs = HtmlXPathSelector(response)
	# 	titles = hxs.select('//div[@class="category-description"]')
	# 	items=[]
	# 	for title in titles:
	# 		item = ThreeMusesGlassItem()
	# 		item["title"] = title.select("text()").extract()
	# 		#item["url"] = url.select("a/@href").extract()
	# 		items.append(item)

	# 	return items

# class WikiSpider(BaseSpider):

# 	#name the spider
# 	name = 'wikipedia'

# 	#allowed domains to scrape
# 	allowed_domains = ["en.wikipedia.org/"]

# 	#urls the spider beings to crawl from
# 	start_urls = ["http://en.wikipedia.org/wiki/Category:2014_films"]

# 	#parses and returns the scraped data
# 	def parse(self, response):
# 		hxs = HtmlXPathSelector(response)
# 		titles = hxs.select('//div[@class="title"]')
# 		items=[]
# 		for title in titles:
# 			item = WikiItem()
# 			item["movie_title"] = title.select("a/text()").extract()
# 			item["movie_url"] = title.select("a/@href").extract()
# 			items.append(item)

# 		return items