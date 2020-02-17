# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class EpubdownPipeline(object):
    def process_item(self, item, spider):
        item["link"]="https://www.aixdzs.com"+item['link']

        with open('./chaoccss2.csv','a') as f:
            f.write(item['name']+"     "+item['link']+'\n')
            f.close()
        return item
