from django.shortcuts import render
from .models import OnyxDecoration, ResinDecoration

# Create your views here.

def onyx_decorations_view(request):
    produse = OnyxDecoration.objects.all()
    context = {
          'produse': produse
	}
    return render(request, 'onyx_decorations.html', context)


def onyx_decorations_details_view(request, slug):   

    try:
        produs = OnyxDecoration.objects.get(slug=slug)
    except OnyxDecoration.DoesNotExist:
        produs = None
    
    context = {
        'produs': produs
        }

    return render(request, 'decoratiuni/onyx_decorations_details.html', context)



def resin_decorations_view(request):
    produse = ResinDecoration.objects.all()
    context = {
          'produse': produse
	}
    return render(request, 'resin_decorations.html', context)


def resin_decorations_details_view(request, slug):
    try:
        produs = ResinDecoration.objects.get(slug=slug)
    except ResinDecoration.DoesNotExist:
        produs = None

    context = {
        'produs': produs
    }
    return render(request, 'resin_decorations_details.html', context)
