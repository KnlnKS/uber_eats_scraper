import scrapy
import json
import re

from os.path import dirname
from scrapy.selector import Selector

from ..items import NeighbourhoodItem


class NeighbourhoodsSpider(scrapy.Spider):
    name = 'neighbourhoods'

    def __init__(self, city='', country='', **kwargs):
        if city is '' and country is '':
            regions_file = open(dirname(__file__) + "/../../output/regions.json")
            regions = json.load(regions_file)

            self.start_urls = []
            for i in range(len(regions["cities"])):
                parsed = regions["cities"][i]["href"].split('/')
                self.start_urls.append(
                    "https://www.ubereats.com/" + parsed[1] + "/category/" + parsed[len(parsed) - 1] + "/location")
        else:
            self.start_urls = ['https://www.ubereats.com/ca/category/' + city]

        super().__init__(**kwargs)

    def parse(self, response):
        sel = Selector(response)
        content = sel.xpath('//*[@id="__REACT_QUERY_STATE__"]/text()').getall()[0].replace("\\u0022", '"')
        fixed_content = re.sub(r',"queryHash":"\[(.*?)\]"', '', content)
        query_data = json.loads(fixed_content)
        neighbourhood_data = query_data["queries"][0]["state"]["data"]["navigationLinks"][3]["subNav"]

        items = NeighbourhoodItem()

        for i in range(len(neighbourhood_data)):
            items["title"] = neighbourhood_data[i]["text"].replace(" food delivery", "")
            items["href"] = neighbourhood_data[i]["href"]

            yield items
