from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	artwork = Artwork.objects.all()
	form = ArtworkForm()
	return render(request, 'home.html', {'artwork': artwork, 'form': form, } )

