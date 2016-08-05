import scrapy
import django
django.setup()

from scrapper.items import ArticleItem, AuthorItem


class TechCrunchSpider(scrapy.Spider):
    name = "tech_crunch"
    allowed_domains = ["techcrunch.com"]
    start_urls = [
        "http://techcrunch.com/"
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="river1"]/li'):
            author = AuthorItem()
            author['name'] = sel.xpath('div/div[2]/div[1]/a/text()').extract()
            author['link'] = sel.xpath('div/div[2]/div[1]/a/@href').extract()
            author_model = author.save()
            
            article = ArticleItem()
            article['title'] = sel.xpath('div/div[2]/h2/a/text()').extract()
            article['link'] = sel.xpath('div/div[2]/h2/a/@href').extract()
            article['content'] = sel.xpath('div/div[2]/p/text()').extract()
            article['publication_date'] = sel.xpath(
                'div/div[2]/div[1]/time/@datetime'
            ).extract()
            article['author'] = author_model
            article.save()
            