# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem

from scrapper.models import Article, Author


class ArticleItem(DjangoItem):
    django_model = Article


class AuthorItem(DjangoItem):
    django_model = Author