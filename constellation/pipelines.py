# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem

#每天爬下來的資料表獨立為一個 Table
CONSTELLATION = f'constellation {datetime.now().strftime("%Y%m%d")}'

class ConstellationPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  

    def process_item(self, item, spider):
        item['date'] = datetime.strptime(item['date'],"%Y-%m-%d")
        postItem = dict(item)
        self.db[CONSTELLATION].insert(postItem)
        return item
 
 #以日期作為參照，避免在同一天重複抓取資料
class DuplicatesTitlePipeline(object):
    def __init__(self):
        self.article = set()
    def process_item(self, item, spider):
        date = item['date'] 
        if date in self.article:
            raise DropItem('duplicates data found !')
        self.article.add(date)
        return(item)

