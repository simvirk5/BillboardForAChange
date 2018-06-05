from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	# CATEGORY_TEXT_CHOICES = (
	# 		('funny', 'Funny'),
	# 		('inspirational', 'Inspirational'),
	# 		('political', 'Political'),
	# 		('sarcasm', 'Sarcasm'),
	# 		('courage', 'Courage'),
	# 		('music', 'Music'),
	# 		('happy', 'Happy'),
	# 		('hope', 'Hope'),
	# 		('peace', 'Peace'),
	# 		('outdoors', 'Outdoors'),
	# 	)
	# category_text = models.CharField(max_length=100, choices=CATEGORY_TEXT_CHOICES)
	# artist = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.name

class Artwork(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	inspiration = models.TextField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	artist = models.ForeignKey(User, on_delete=models.CASCADE) 
	image = models.ImageField(upload_to='items/%Y/%m/%d', blank=True)
	
	def __str__(self):
		return self.title


