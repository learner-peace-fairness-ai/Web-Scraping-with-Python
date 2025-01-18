from scrapy import Spider
from wikiSpider.items import Article


class ArticleSpider(Spider):
    name = 'article'
    allowed_domain = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Main-Page',
        'http://en.wikipedia.org/wiki/Python_%28programming_language%29']

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1//text()').get()

        print(f'Title is: {title}')
        item['title'] = title
        return item
