from django.shortcuts import render, redirect
from .models import WaxArrangement

# Create your views here.


def wax_arrangements_view(request):
    produse = WaxArrangement.objects.all()
    context = {
        'produse': produse
    }
    return render(request, 'aranjamente_ceara/wax_arrangements.html', context)


def wax_arrangement_details_view(request, slug):
   

    try:
        produs = WaxArrangement.objects.get(slug=slug)
    except WaxArrangement.DoesNotExist:
        produs = None

    context = {
        'produs': produs
    }

    return render(request, 'aranjamente_ceara/wax_arrangements_details.html', context )





