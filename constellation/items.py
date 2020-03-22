# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ConstellationItem(scrapy.Item):
    date = scrapy.Field()
    constellations = scrapy.Field()
    total = scrapy.Field()
    love = scrapy.Field()
    work = scrapy.Field()
    money = scrapy.Field()
