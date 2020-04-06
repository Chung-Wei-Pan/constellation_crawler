FROM python:3.6.10
MAINTAINER Leo
WORKDIR /home/python/constellation
COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt
COPY . .
CMD [ "scrapy","crawl","constellation" ]
