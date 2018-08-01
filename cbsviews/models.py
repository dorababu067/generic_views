from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
	title		= models.CharField(max_length=256)
	pricipal	= models.CharField(max_length=256)
	location	= models.CharField(max_length=256)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('cbsviews:list')
