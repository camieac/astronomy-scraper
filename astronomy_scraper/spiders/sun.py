# -*- coding: utf-8 -*-
import scrapy
from astronomy_scraper.items import DayConditions
import re
import astronomy_scraper.utils as utils


class SunSpider(scrapy.Spider):
    name = "sun"
    allowed_domains = ["http://www.timeanddate.com/"]
    start_urls = (
        'http://www.timeanddate.com/sun/usa/new-york?month=4&year=2016',
    )

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        item = DayConditions()
        pattern = re.compile(u"<.*?>|&nbsp;|&amp;|\u260e|\xa0|\xb0C",re.DOTALL|re.M)
        item['sunrise'] = response.xpath('//tr[@class="hl" and @data-day="3"]/td/text()').extract()[0]
        item['sunset'] = response.xpath('//tr[@class="hl" and @data-day="3"]/td/text()').extract()[2]
        item['day_length'] = response.xpath('//tr[@class="hl" and @data-day="3"]/td/text()').extract()[4]
        item['day_difference'] = response.xpath('//tr[@class="hl" and @data-day="3"]/td/text()').extract()[5]
        item['twil_astro_start'] = response.xpath('//tr[@class="hl" and @data-day="3"]/td/text()').extract()[6]
        item['twil_astro_end'] = response.xpath('//tr[@class="hl" and @data-day="3"]/td/text()').extract()[7]
        item['twil_naut_start'] = response.xpath('//tr[@class="hl" and @data-day="3"]/td/text()').extract()[8]
        item['twil_naut_end'] = response.xpath('//tr[@class="hl" and @data-day="3"]/td/text()').extract()[9]
        item['twil_civil_start'] = response.xpath('//tr[@class="hl" and @data-day="3"]/td/text()').extract()[10]
        item['twil_civil_end'] = response.xpath('//tr[@class="hl" and @data-day="3"]/td/text()').extract()[11]
        # response.xpath('//div[@id="qfacts"]/p/text()').extract()[2]
        #re.sub(pattern, "", temperature)
        #Get today's temperature

        return item
