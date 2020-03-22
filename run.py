import subprocess
import schedule
import datetime
from  scrapy  import cmdline

 
def crawl_work():
    cmdline.execute('scrapy crawl constellation'.split())

if __name__ == '__main__': 

    print('目前時間{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %h %H:%M:%S')))
    schedule.every(1).hours.do(crawl_work) 

    while True:
        schedule.run_pending()