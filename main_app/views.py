from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Artwork, Category
from .forms import LoginForm, SignUpForm, ArtworkForm
# from .filters import ArtworkFilter

def index(request):
	return render(request, 'index.html')
	

def profile(request):
	if request.user.is_authenticated:
		categories = Category.objects.values()
		artwork = Artwork.objects.filter(artist=request.user)
		print('CATS FOUND', categories)
		return render(request, 'profile.html', {'artwork': artwork, 'categories': categories})
	else:
		return HttpResponseRedirect('/login')
# def new_post(request):
# 	form = ArtworkForm(request.POST)
# 	if form.is_valid() and request.user:
# 		artwork = form.save(commit = False)
# 		artwork.user = request.user
# 		artworks.save()
#         return HttpResponseRedirect('profile')
# 	else:
# 		form = ArtworkForm()
# 	return render(request, 'new_post.html', {'form': form})

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
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



#     class PartyCreate(CreateView):
# 	model = Party
# 	fields = ["title", "location", "description"]
# 	success_url = reverse_lazy("party_list")

# class PartyDelete(DeleteView):
# 	model = Party
# 	success_url = reverse_lazy("party_list")

# class PartyUpdate(UpdateView):
#     model = Party
#     fields = ["title", "location", "description"]
#     success_url = reverse_lazy("party_list")