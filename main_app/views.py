from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Artwork
from .forms import LoginForm, SignUpForm, ArtworkForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# from django import forms
# from cloudinary.forms import cl_init_js_callbacks      
# from .models import Photo
# from .forms import PhotoForm

# import cloudinary
# import cloudinary.uploader
# import cloudinary.api


def index(request):
	return render(request, 'index.html')

def test(request):
	print('test run')

def profile(request):
	artwork = Artwork.objects.all()
	return render(request, 'profile.html', {'artwork': artwork})


def post_artwork(request):
	print('request.user', request.user.id)
	print('should be whole thing', request.POST)
	title = request.POST['title']
	description = request.POST['description']
	inspiration = request.POST['inspiration']
	category = request.POST['dropdown']
	# category = request.POST['category']
	# form = ArtworkForm(request.POST)
	# category = form['value']
	# category = request.POST.get('category')
	image = request.POST['image']
	print('POST IS', request.POST)
	new_entry = Artwork.objects.create(title=title, description=description, inspiration=inspiration, category=category, image=image, artist=request.user)
	print(new_entry)

	return HttpResponseRedirect('/profile')


def profile(request):
	if request.user.is_authenticated:
		# categories = Category.objects.values()
		artwork = Artwork.objects.filter(artist=request.user.id).values()
		# print('Artwork found', artwork)
		return render(request, 'profile.html', {'artwork': artwork})
	else:
		return HttpResponseRedirect('/login')		

# def profile(request):
# 	if request.method == 'POST':
# 		form = ArtworkForm(request.POST)
# 		if form.is_valid() and request.user:
# 			artwork = form.save(commit=False)
# 			artwork.user = request.user
# 			artwork.save()
# 			return redirect('profile')
# 	else:
# 		form = ArtworkForm(request.user)
# 	return render(request, 'profile.html', {'form': form})


def search(request):
    # category_id = request.POST['selectionbox']
    category_id = request.POST.get("selectionbox")
    print('category id', category_id, 'request', request.POST)
    artwork = Artwork.objects.filter(category=category_id)
    print('artwork', artwork)
    return render(request, 'search.html', {'artwork': artwork})


# class PartyDelete(DeleteView):
# 	model = Party
# 	success_url = reverse_lazy("party_list")




# def show(request, artwork_id):
# 	cat = None
# 	try: 
# 		artwork = Artwork.objects.get(id=artwork_id)
# 	except: 
# 		pass
# 	return render(request, 'show.html', {'artwork': artwork})



def login_view(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user. is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else: 
					print("the account has been disabled.")
	else:
		form = LoginForm()
		return render(request, 'login.html', {'form': form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            email = form.cleaned_data['email']
            user = User.objects.create_user(username, password, email)
            # user = authenticate(username=username, password=password1)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
    	form = SignUpForm()
    	return render(request, 'signup.html', {'form': form})


def delete(request, artwork_id):
	Artwork.objects.filter(id=artwork_id).delete()
	return HttpResponseRedirect('/profile')




# def upload(request):
# 	context = dict( backend_form = PhotoForm())
# 	cloudinary.uploader.upload(request.FILES['file'])

# 	if request.method == 'POST':
# 		form = PhotoForm(request.POST, request.FILES)
# 		context['posted'] = form.instance

# 		if form.is_valid():
# 			form.save()

# 	return render(request, 'upload.html', context)

