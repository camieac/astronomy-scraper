# -*- coding: utf-8 -*-
import scrapy
from astronomy_scraper.items import DayConditions
import re
import astronomy_scraper.utils as utils
from astronomy_scraper.lists import Locations
import datetime


class WundergroundSpider(scrapy.Spider):
    name = "wunderground_weather"

    def __init__(self, location=Locations.london, datetime=datetime.datetime.now(), *args, **kwargs):
        super(WeatherSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://api.wunderground.com/api/%s/geolookup/conditions/q/%s/%s.json' % ( settings.WUNDERGROUND_API_KEY, location.country.abbreviation, location.name)
        ]
        self.datetime = datetime
        self.allowed_domains = ["http://api.wunderground.com/"]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        json_response = json.loads(response.body_as_unicode())
        item = DayConditions()
        print json_response


        return item
