from django.shortcuts import render
from aranjamente_flori.models import NaturalFlower
from aranjamente_flori.models import ArtificialFlower
from aranjamente_ceara.models import WaxArrangement
from decoratiuni.models import OnyxDecoration, ResinDecoration

# Create your views here.



def home_view(request):
    return render(request, 'home/home.html')

def despre_view(request):
    return render(request, 'home/despre.html' )

def categorii_view(request):
    return render(request, 'home/categorii.html')

def search_view(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        results = (
            list(NaturalFlower.objects.filter(name__icontains=query)) +
            list(ArtificialFlower.objects.filter(name__icontains=query)) +
            list(WaxArrangement.objects.filter(name__icontains=query)) +
            list(OnyxDecoration.objects.filter(name__icontains=query)) +
            list(ResinDecoration.objects.filter(name__icontains=query))
        )

        for product in results:
            if isinstance(product, NaturalFlower):
                product.type = 'natural'
            elif isinstance(product, ArtificialFlower):
                product.type = 'artificial'
            elif isinstance(product, WaxArrangement):
                product.type = 'wax'
            elif isinstance(product, OnyxDecoration):
                product.type = 'onyx'
            elif isinstance(product, ResinDecoration):
                product.type = 'resin'

    return render(request, "home/search_results.html", {"query": query, "results": results})

