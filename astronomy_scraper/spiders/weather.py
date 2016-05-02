# -*- coding: utf-8 -*-
import scrapy
from astronomy_scraper.items import DayConditions
import re

class WeatherSpider(scrapy.Spider):
    name = "weather"
    allowed_domains = ["http://www.timeanddate.com/"]
    start_urls = (
        'http://www.timeanddate.com/weather/usa/new-york',
    )

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        item = DayConditions()
        pattern = re.compile(u"<.*?>|&nbsp;|&amp;|\u260e|\xa0|\xb0C",re.DOTALL|re.M)
        temperature = response.xpath('//div[@class="h2"]/text()').extract_first()#.re(r'(\d+..C)')[0]#.strip('\xa0\xb0c')
        re.sub(pattern, "", temperature)
        #Get today's temperature
        item['temperature'] = temperature
        return item
