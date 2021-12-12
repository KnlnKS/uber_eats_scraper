import scrapy
import json
import re

from os.path import dirname
from scrapy.selector import Selector

from ..items import RegionItem


class RegionSpider(scrapy.Spider):
    name = 'regions'

    def __init__(self, country='', **kwargs):
        if country is '':
            countries_file = open(dirname(__file__) + "/../../output/countries.json")
            countries = json.load(countries_file)

            self.start_urls = []
            for i in range(len(countries)):
                self.start_urls.append("https://www.ubereats.com" + countries[i]["href"] + "/location")
        else:
            self.start_urls = ['https://www.ubereats.com/' + country + '/location']

        super().__init__(**kwargs)

    def parse(self, response):
        sel = Selector(response)
        content = sel.xpath('//*[@id="__REACT_QUERY_STATE__"]/text()').getall()[0].replace("\\u0022", '"')
        fixed_content = re.sub(r',"queryHash":"\[(.*?)\]"', '', content)
        query_data = json.loads(fixed_content)
        region_data = query_data["queries"][1]["state"]["data"]["regionCityLinks"]["links"]

        items = RegionItem()

        for i in range(len(region_data)):
            items["title"] = region_data[i]["title"]
            items["href"] = region_data[i]["href"]
            items["cities"] = region_data[i]["links"]

            yield items
