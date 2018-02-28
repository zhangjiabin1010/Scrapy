# -*- coding: utf-8 -*-
import scrapy
from Meizitu.items import MeizituItem

class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    start_urls = ['http://pic.yesky.com/c/6_20491.shtml']

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        # list = response.xpath('//ol[@class="commentlist"]')
        # for li in list:
        item = MeizituItem()
        item['image'] = sel.xpath('//div[@class="wrap2"]/div/div/dl/dt/a/img/@src').extract()


        #item['image'] = response.xpath("./li//img/@src").extract()

        yield item
