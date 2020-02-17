# -*- coding: utf-8 -*-
import scrapy
from epubdown.items import EpubdownItem

class EbuplinkSpider(scrapy.Spider):
    name = 'ebuplink'
    # allowed_domains = ['https://www.aixdzs.com/']
    start_urls = ['https://www.aixdzs.com/sort/16/index_0_2_0_2.html']

    def parse(self, response):
        resall = response.css(".b_name a::attr(href)").getall()
        for res in resall:

            yield response.follow(url=res,callback=self.new_parse)
    
    def new_parse(self,response):
        item = EpubdownItem()
        name = response.css(".d_info h1::text").get()
        link = response.css("#epub_down a::attr(href)").getall()
        try:
            link=link[0]
            item['link']=link
        except:
            pass
        item['name']=name
        
        yield item
    