# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomeItem(scrapy.Item):
    # define the fields for your item here like:
    # 标题
    title = scrapy.Field()
    # 网址
    url = scrapy.Field()
    # 简介
    jianjie = scrapy.Field()

    word = scrapy.Field()

    image = scrapy.Field()

   
