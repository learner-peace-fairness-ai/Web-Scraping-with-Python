from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from wikiSpider.items import Article
from scrapy.linkextractors import LinkExtractor


class ArticleCrawlSpider(CrawlSpider):
    name = 'article_crawl'
    allowed_domain = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Python_%28programming_language%29']
    rules = [Rule(LinkExtractor(allow=(r'(/wiki/)((?!:).)*$')), callback='parse_item', follow=True)]

    def parse_item(self, response):
        item = Article()
        title = response.xpath('//h1//text()').get()

        print(f'Title is: {title}')
        item['title'] = title
        return item
