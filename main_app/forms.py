from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Artwork, Category

class ArtworkForm(forms.ModelForm):
	class Meta:
		model = Artwork
		fields = ['title', 'description', 'inspiration', 'category']

class LoginForm(forms.Form):
	username = forms.CharField(label="User Name", max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30, required=False)
	email = forms.EmailField(max_length=254)
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password' )
