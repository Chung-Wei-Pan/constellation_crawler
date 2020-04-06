import subprocess
import schedule
import datetime
from  scrapy  import cmdline

 
def crawl_work():
    # cmdline.execute('scrapy crawl constellation'.split())
    # cmdline.execute('sudo service mongod start'.split())
    # cmdline.execute('sudo systemctl start mongodb'.split())

if __name__ == '__main__': 

    print('目前時間{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %h %H:%M:%S')))
    schedule.every(1).seconds.do(crawl_work) 

    while True:
        schedule.run_pending()