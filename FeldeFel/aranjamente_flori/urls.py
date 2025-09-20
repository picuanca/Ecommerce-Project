from django.urls import path
from .views import artificial_flowers_view
from .views import natural_flowers_view
from .views import natural_flowers_details_view
from .views import artificial_flowers_details_view

app_name = "aranjamente_flori"

urlpatterns = [

	path("naturale", natural_flowers_view, name="naturale"),
	path("artificiale", artificial_flowers_view, name="artificiale"),
    path("naturale/<slug:slug>/", natural_flowers_details_view, name="detalii"),
    path("artificiale/<slug:slug>/", artificial_flowers_details_view, name="artificiale_detalii")
    
]
