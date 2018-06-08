from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


# class Photo(models.Model):
# 	image = CloudinaryField('image')

# class Category(models.Model):
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
	# name = models.CharField(max_length=100, default='')

	# def __str__(self):
	# 	return self.name

class Artwork(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	inspiration = models.TextField()
	category = models.CharField(max_length=100)
	artist = models.ForeignKey(User, on_delete=models.CASCADE) 
	image = models.CharField(max_length=1000)



	def __str__(self):
		return self.title


