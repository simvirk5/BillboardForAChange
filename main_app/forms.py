from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Artwork
from django.forms import ModelForm      
# from .models import Photo
# from cloudinary.models import CloudinaryField


class ArtworkForm(forms.ModelForm):
	class Meta:
		model = Artwork
		fields = ['category', 'title', 'description', 'inspiration', 'image']

		# fields = ['title']
	# category = forms.ModelChoiceField(queryset=Category.objects.all())




# class ArtworkForm(forms.Form):
# 	category=forms.CharField(label="what is your category", widget=forms.Select(choices=CATEGORY_TEXT_CHOICES))


class LoginForm(forms.Form):
	username = forms.CharField(label="User Name", max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(forms.Form):
	# first_name = forms.CharField(max_length=30)
	# last_name = forms.CharField(max_length=30, required=False)
	username = forms.CharField(label="User Name", max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())
	email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput())
	


# class PhotoForm(ModelForm):
# 	class Meta:
# 		model = Photo
		
