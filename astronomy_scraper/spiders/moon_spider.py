# -*- coding: utf-8 -*-
import scrapy


class MoonSpider(scrapy.Spider):
    name = "moon"
    allowed_domains = ["http://www.timeanddate.com/moon/phases/uk/london"]
    start_urls = (
        'http://www.timeanddate.com/moon/phases/uk/london',
    )

    def parse(self, response):
        item = scrapy.AstronomyDay()
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        pass
