# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CountryItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()


class RegionItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    cities = scrapy.Field()


class NeighbourhoodItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()


class CategoryItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()
