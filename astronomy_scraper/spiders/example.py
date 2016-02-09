# -*- coding: utf-8 -*-
import scrapy
from astronomy_scraper.items import DayConditions

class MoonPhaseSpider(scrapy.Spider):
    name = "moon_phase"
    allowed_domains = ["http://www.timeanddate.com/"]
    start_urls = (
        'http://www.timeanddate.com/moon/phases/uk/london',
        'http://www.timeanddate.com/weather/usa/new-york'
    )

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        item = DayConditions()
        # Get today's moon phase
        item['moon_phase'] = float(response.xpath('//div[@class="h1"]/text()').re(r'Moon: (\d+\.\d+)')[0])

        
        return item
