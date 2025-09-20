from django.urls import path
from .views import wax_arrangements_view
from .views import wax_arrangement_details_view


app_name = "aranjamente_ceara"

urlpatterns = [

	path("ceara", wax_arrangements_view, name="wax_arrangements_url"),
    path("ceara/<slug:slug>/", wax_arrangement_details_view, name="wax_arrangement_details_url")
    
]

