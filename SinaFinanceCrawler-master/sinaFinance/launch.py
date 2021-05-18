# -*- coding:utf-8 -*-
from scrapy import cmdline
from sinaFinance.scrapy_redis import BloomfilterOnRedis
cmdline.execute("scrapy crawl sina".split())