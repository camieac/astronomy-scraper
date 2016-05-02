# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AstronomyLocation(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    altitude = scrapy.Field()
    pass

class AstronomyDay(scrapy.Item):
    id = scrapy.Field()
    day = scrapy.Field()
    date = scrapy.Field()
    precipitation = scrapy.Field()
    humidity = scrapy.Field()
    wind = scrapy.Field()
    moon = scrapy.Field()
    pass


class DayConditions(scrapy.Item):
    moon_phase = scrapy.Field()
    temperature = scrapy.Field()
