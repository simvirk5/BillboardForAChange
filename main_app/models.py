from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	CATEGORY_TEXT = (
			('funny', 'Funny'),
			('inspirational', 'Inspirational'),
			('political', 'Political'),
			('parksandRec', 'ParksandRec'),
			('sarcasm', 'Sarcasm'),
			('courage', 'Courage'),
			('music', 'Music'),
			('happy', 'Happy'),
			('hope', 'Hope'),
			('peace', 'Peace'),
		)
	category_text = models.CharField(max_length=100, choices=CATEGORY_TEXT)

class Artwork(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	inspiration = models.TextField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	artist = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title



