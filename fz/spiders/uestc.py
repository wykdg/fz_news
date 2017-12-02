# -*- coding: utf-8 -*-
import scrapy

from fz.items import FzItem


class UestcSpider(scrapy.Spider):
    name = "uestc"
    allowed_domains = ["www.news.uestc.edu.cn"]
    start_urls = ['http://www.news.uestc.edu.cn/']

    def parse(self, response):
        hrefs=response.xpath('//*[@id="menu"]/ul/li/a/@href')
        for href in hrefs:
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_news_page)


    def parse_news_page(self,response):
        next_page=response.xpath('//li[@class="move-page "]/a/@href')
        if next_page:
            full_url = response.urljoin(next_page[-1].extract())
            yield scrapy.Request(full_url, callback=self.parse_news_list)
            yield scrapy.Request(full_url, callback=self.parse_news_page)

    def parse_news_list(self,response):
        news_list=response.xpath('//*[@id="Degas_news_list"]/ul/li[3]/h3/a/@href')
        for news in news_list:
            full_url = response.urljoin(news.extract())
            yield scrapy.Request(full_url, callback=self.parse_news)

    def parse_news(self,response):
        data1 = response.xpath( '//*[@class="Degas_news_title"]/text()').extract()
        title=u'\n'.join(data1)
        paragraphs=response.xpath('//*[@class="Degas_news_content"]/p/text()').extract()

        content=u'\n'.join(paragraphs)
        result=FzItem()
        result['title']=title
        result['content']=content
        yield result
