# -*- coding: utf-8 -*-
import scrapy
from Autohome.items import AutohomeItem
class AutohomeSpider(scrapy.Spider):
    name = 'autohome'
    start_urls = ['https://www.autohome.com.cn/all/']

    def parse(self, response):
#返回该表达式对应的所有selector list列表
        tit_list = response.xpath("//div[@class='article-wrapper']/ul/li/a")
        for tit in tit_list:
            item = AutohomeItem()
            #extract（）序列化为unicode字符串
            item['title'] = tit.xpath("./h3/text()").extract()[0]
            item['url'] = tit.xpath("./@href").extract()[0]
            item['jianjie'] = tit.xpath("./p/text()").extract()[0]
            #遍历网址，追加给parse_2处理
            for url in tit.xpath("./@href").extract():
                yield scrapy.Request("https:" + url,meta = {'key' : item},callback=self.parse_2)
            #抓取下一页
        if len(response.xpath("//a[@class ='page-item-next page-disabled']")) == 0:
            next_url = response.xpath("//a[@class ='page-item-next']/@href").extract()[0]
            yield scrapy.Request("https://www.autohome.com.cn" + next_url, callback=self.parse)

    def parse_2(self, response):
        #文章详解
        #传递parse的参数到parse_2
        item = response.meta['key']
        if len(response.xpath("//div[@id='articleContent']")) != 0:
            item['word'] = response.xpath("string(//div[@id='articleContent'])").extract()[0]
        item['image'] = response.xpath("//div[@class='area article']//img/@src").extract()
        yield item




