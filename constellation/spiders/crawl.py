import scrapy
from bs4 import BeautifulSoup
import datetime
import time
import os
from ..items import ConstellationItem

class Constellation(scrapy.Spider):
    name = 'constellation'
    start_urls = ['http://astro.click108.com.tw/daily_0.php?iAcDay=2020-03-21&iAstro=0']
    url = 'http://astro.click108.com.tw/daily_'
    today = str(datetime.date.today())
    def parse(self,response):
        items = ConstellationItem()
        
        for query in response.css('.LEFT'):
            items['date'] = self.today
            items['constellations'] = query.css('.HOROSCOPE_BTN li>h3::text').extract()
            items['total'] = str(query.css('.TODAY_CONTENT > h3 + p span::text').extract()) + str(query.css('.TODAY_CONTENT  p:nth-child(3)::text').extract())
            items['love'] = str(query.css('.TODAY_CONTENT > p:nth-child(4) span::text').extract()) + str(query.css('.TODAY_CONTENT  p:nth-child(5)::text').extract())
            items['work'] = str(query.css('.TODAY_CONTENT > p:nth-child(6) span::text').extract()) + str(query.css('.TODAY_CONTENT  p:nth-child(7)::text').extract())
            items['money'] = str(query.css('.TODAY_CONTENT > p:nth-child(8) span::text').extract()) + str(query.css('.TODAY_CONTENT  p:nth-child(9)::text').extract())
            if items['constellations']:
                yield(items)
        for n in range(1,12):
            new_url = self.url + str(n) + '.php?iAcDay='+ self.today + '&iAstro=' + str(n)
            yield scrapy.Request(new_url,callback=self.parse)
        # while True:
        #     os.sys