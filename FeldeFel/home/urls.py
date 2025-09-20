from django.urls import path
from home.views import home_view
from home.views import despre_view
from home.views import categorii_view
from home.views import search_view

app_name = "home"

urlpatterns = [
    path("", home_view, name="home"), 
    path("despre", despre_view, name="despre"),
    path("categorii/", categorii_view, name="categorii"),
    path("search/", search_view, name="search"),
]
