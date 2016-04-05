# -*- coding: utf-8 -*-
import scrapy
from astronomy_scraper.items import MoonPhaseSnippet


class MoonPhaseSpider(scrapy.Spider):
    name = "moon_phase"
    allowed_domains = ["http://www.timeanddate.com/"]
    start_urls = (
        'http://www.timeanddate.com/moon/phases/usa/new-york?year=2016',
    )

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        item = MoonPhaseSnippet()
        # Get today's moon phase
        item['moon_phase_date'] = response.xpath('//tr[@class="c0"]/td/text()').extract()[6]
        item['moon_phase_time'] = response.xpath('//tr[@class="c0"]/td/text()').extract()[7]
        item['moon_phase_duration'] = response.xpath('//tr[@class="c0"]/td/text()').extract()[8]
        return item
