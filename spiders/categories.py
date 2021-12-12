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
        fixedContent = re.sub(r',"queryHash":"\[(.*?)\]"', '', content)
        queryData = json.loads(fixedContent)
        categoryData = queryData["queries"][0]["state"]["data"]["navigationLinks"][0]["subNav"]

        for i in range(len(categoryData)):
            categoryData[i]["text"] = re.sub(r' Delivery in [^\\]*', '', categoryData[i]["text"])
            categoryData[i].pop("imgSrc")
            categoryData[i].pop("rank")
            categoryData[i].pop("iconUrl")
            categoryData[i].pop("backgroundColor")
            categoryData[i].pop("label")
            categoryData[i].pop("isAnchor")
