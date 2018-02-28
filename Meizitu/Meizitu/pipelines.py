# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class Images(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image in item['image']:
            yield scrapy.Request(image)
