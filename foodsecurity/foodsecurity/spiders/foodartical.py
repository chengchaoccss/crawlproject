# -*- coding: utf-8 -*-
import scrapy
from foodsecurity.items import FoodsecurityItem

class FoodarticalSpider(scrapy.Spider):
    name = 'foodartical'
    #allowed_domains = ['http://www.foodmate.net/']
    start_urls = ['http://www.foodmate.net/jianyan/1361/list_'+str(i)+'.html' for i in range(1,31)]

    def parse(self, response):
        try:
            item=FoodsecurityItem()
            articles= response.css(".catlist_li")
            for article in articles:
                name = article.css("a::text").get()
                link = article.css("a::attr(href)").get()
                item['name']=name
                item['link']=link
                yield item
        except:
            pass

