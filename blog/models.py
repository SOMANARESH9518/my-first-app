from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class  Post(models.Model):
	"""docstring for  Post"models.Model"""
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank = True,null = True)

	def __init__(self, arg):
		super( Post,self).__init__()
		self.arg = arg
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

# Create your models here.
