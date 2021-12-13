import scrapy
import json
import re

from os.path import dirname
from scrapy.selector import Selector

from ..items import CategoryItem


class CategoriesSpider(scrapy.Spider):
    name = 'categories'

    def __init__(self, city='', country='', **kwargs):
        if country is '':
            regions_file = open(dirname(__file__) + "/../../output/regions.json", encoding='utf-8')
            regions = json.load(regions_file)
            self.start_urls = []

            for i in range(len(regions)):
                for j in range(len(regions[i]["cities"])):
                    parsed = regions[i]["cities"][j]["href"].split("/")
                    self.start_urls.append(
                        "https://www.ubereats.com/" + parsed[1] + '/category/' + parsed[len(parsed) - 1])
        else:
            self.start_urls = ['https://www.ubereats.com/' + country + '/category/' + city]

        super().__init__(**kwargs)

    def parse(self, response):
        sel = Selector(response)
        content = sel.xpath('//*[@id="__REACT_QUERY_STATE__"]/text()').getall()[0].replace("\\u0022", '"')
        fixed_content = re.sub(r',"queryHash":"\[(.*?)\]"', '', content)
        query_data = json.loads(fixed_content)
        category_data = query_data["queries"][0]["state"]["data"]["navigationLinks"][0]["subNav"]

        items = CategoryItem()

        for i in range(len(category_data)):
            items["title"] = re.sub(r' Delivery in [^\\]*', '', category_data[i]["text"]).replace("categories.seo.", "")

            yield items
