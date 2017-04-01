# -*- coding: utf-8 -*-
import scrapy
from astronomy_scraper.items import DayConditions
import re
import astronomy_scraper.utils as utils
from astronomy_scraper.lists import Locations
import datetime


class WeatherSpider(scrapy.Spider):
    name = "weather"

    def __init__(self, location=Locations.london, datetime=datetime.datetime.now(), *args, **kwargs):
        super(WeatherSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://www.timeanddate.com/weather/%s/%s/ext' % (location.country.abbreviation, location.name)
        ]
        self.datetime = datetime
        self.allowed_domains = ["http://www.timeanddate.com/"]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        item = DayConditions()
        pattern = re.compile(u"<.*?>|&nbsp;|&amp;|\u260e|\xa0|\xb0C",re.DOTALL|re.M)
        temperature = response.xpath('//div[@class="h2"]/text()').extract_first()#.decode('unicode_escape').encode('ascii','ignore')
        temperature = utils.strip_non_ascii(temperature)
        re.sub(pattern, "", temperature)
        # Get today's temperature
        item['temperature'] = temperature
        item['date'] = response.xpath('//div[@id="qfacts"]/p/text()').extract()[2]

        # Get 14 day forecast data for particular datetime
        print response.body
        item['temp_high'] = response.xpath("//div[contains(concat(' ',normalize-space(@class),' '),' temp low ')]/text()").extract_first()#.replace('Hi:', '')
        return item
