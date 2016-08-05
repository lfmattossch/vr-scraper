from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=100)
	link = models.TextField()

class Article(models.Model):
	title = models.TextField()
	link = models.TextField()
	content = models.TextField()
	publication_date = models.CharField(max_length=100)
	author = models.ForeignKey(Author)
