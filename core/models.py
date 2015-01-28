# -*- coding:utf-8 -*-
from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 100)
	message = models.TextField()
	date_publication = models.DateTimeField()

	def __str__(self):
		return self.title

	def publication_today(self):
		if(self.date_publication.date() == datetime.date.today()):
			return "Yes"
		else:
			return "No"

class Comment(models.Model):
	name = models.CharField(max_length = 400)
	comment = models.TextField()
	date_publication = models.DateTimeField()
	post = models.ForeignKey(Post)

	def __str__(self):
		return self.name

	def publication_today(self):
		if(self.date_publication.date() == datetime.date.today()):
			return "Yes"
		else:
			return "No"						