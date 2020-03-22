# Constellation_crawler
Scrapy 抓取星座網站資訊  

`python run.py`

## Environment
Python 3.6.10  

Scrapy 1.6.0  

MongoDB v3.6.3  


## Schema
|Fields   |Type   |
|---|---|
|_id   |Object   |
|constellations （星座名稱）   |Array   |
|date（日期）   |Date   |
|love（愛情運勢）   |String   |
|money（財務運勢）   |String   |
|total（整體運勢）   |String   |
|work（工作名稱）  |String   |