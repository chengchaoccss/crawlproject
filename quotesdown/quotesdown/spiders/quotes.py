# -*- coding: utf-8 -*-
import scrapy
from quotesdown.items import QuotesdownItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css(".quote")
        for quote in quotes:
            text = quote.css(".text::text").get()
            author = quote.css(".author::text").get()
            tags = quote.css(".tags .tag::text").getall()
            item = QuotesdownItem()
            item['text'] = text
            item['author']=author
            item['tags']=tags
            yield item

            next_page=response.css(".pager .next a::attr(href)").get()
            
        if next_page:
            #next_page = response.urljoin(next_page)
            yield response.follow(url = next_page,callback = self.parse)
           
