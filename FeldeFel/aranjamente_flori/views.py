from django.shortcuts import render
from .models import NaturalFlower
from .models import ArtificialFlower

# Create your views here.

def natural_flowers_view(request):
	produse = NaturalFlower.objects.all()

	context = {
		'produse': produse
		}
	
	return render(request, 'natural_flowers.html', context)


def natural_flowers_details_view(request, slug):	

	try:
		produs = NaturalFlower.objects.get(slug=slug)
	except NaturalFlower.DoesNotExist:
		produs = None

	context = {
		'produs': produs
		}

	return render(request, 'aranjamente_flori/natural_flowers_details.html', context)


def artificial_flowers_view(request):
	produse = ArtificialFlower.objects.all()

	context = {
		'produse': produse
		}

	return render(request, 'aranjamente_flori/artificial_flowers.html', context)


def artificial_flowers_details_view(request, slug):
	try:
		produs = ArtificialFlower.objects.get(slug=slug)

		context = {
			"produs": produs
		}
	except ArtificialFlower.DoesNotExist:
		produs = None

		
	
	return render(request, 'aranjamente_flori/artificial_flowers_details.html', context)

