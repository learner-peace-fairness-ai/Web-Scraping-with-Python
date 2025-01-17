from scrapy import Item
from scrapy import Field


class Article(Item):
    title = Field()