# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduPipeline(object):
    def process_item(self, item, spider):
        print(11111111111111111111111)
        print(item)
