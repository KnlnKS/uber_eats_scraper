import scrapy
from scrapy.selector import Selector
import json
import re


class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    
    def __init__(self, city='', **kwargs):
        self.start_urls = ['https://www.ubereats.com/ca/category/' + city]
        super().__init__(**kwargs)

    def parse(self, response):
        sel = Selector(response)
        content = sel.xpath('//*[@id="__REACT_QUERY_STATE__"]/text()').getall()[0].replace("\\u0022", '"')
        fixed_content = re.sub(r',"queryHash":"\[(.*?)\]"', '', content)
        query_data = json.loads(fixed_content)
        category_data = query_data["queries"][0]["state"]["data"]["navigationLinks"][0]["subNav"]

        for i in range(len(category_data)):
            category_data[i]["text"] = re.sub(r' Delivery in [^\\]*', '', category_data[i]["text"])
            category_data[i].pop("imgSrc")
            category_data[i].pop("rank")
            category_data[i].pop("iconUrl")
            category_data[i].pop("backgroundColor")
            category_data[i].pop("label")
            category_data[i].pop("isAnchor")
