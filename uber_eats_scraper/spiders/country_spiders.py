import scrapy
from scrapy.selector import Selector
import json
import re

from ..items import CountryItem


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    start_urls = ["https://www.ubereats.com/location"]

    def parse(self, response):
        sel = Selector(response)
        content = sel.xpath('//*[@id="__REACT_QUERY_STATE__"]/text()').getall()[0].replace("\\u0022", '"')
        fixed_content = re.sub(r',"queryHash":"\[(.*?)\]"', '', content)
        query_data = json.loads(fixed_content)
        country_data = query_data["queries"][1]["state"]["data"]["countryLinks"]["links"]

        items = CountryItem()

        for i in range(len(country_data)):
            items["title"] = country_data[i]["title"]
            items["href"] = country_data[i]["href"]

            yield items
