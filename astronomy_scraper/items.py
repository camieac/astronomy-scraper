# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AstronomyScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DayConditions(scrapy.Item):
    moon_phase = scrapy.Field()
    temperature = scrapy.Field()
    date = scrapy.Field()
    sunrise = scrapy.Field()
    sunset = scrapy.Field()
    day_length = scrapy.Field()
    day_difference = scrapy.Field()

    # Astronomical Twilight
    twil_astro_start = scrapy.Field()
    twil_astro_end = scrapy.Field()

    # Nautical Twilight
    twil_naut_start = scrapy.Field()
    twil_naut_end = scrapy.Field()

    # Civil Twilight
    twil_civil_start = scrapy.Field()
    twil_civil_end = scrapy.Field()


class MoonPhaseSnippet(scrapy.Item):
    moon_phase_date = scrapy.Field()
    moon_phase_time = scrapy.Field()
    moon_phase_duration = scrapy.Field()

    
