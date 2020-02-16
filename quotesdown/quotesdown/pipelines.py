# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class QuotesdownPipeline(object):
    def process_item(self, item, spider):
        with open('chaoccss.txt','a') as f:
            f.write(item['text']+'----'+item['author']+'----'+item['tags'][0]+'\n')
            f.close()
        return item

