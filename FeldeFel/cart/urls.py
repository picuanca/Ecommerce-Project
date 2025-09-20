from django.urls import path
from .views import cart_view

from .views import add_to_cart_view, erase_cart_view, increase_quantity_view, decrease_quantity_view

app_name= "cart"

urlpatterns = [

	path("", cart_view, name="cart_url"),
    path("add/<slug:slug>", add_to_cart_view, name="add_to_cart_url"),
    path("increase/<slug:slug>/", increase_quantity_view, name="increase_url"),
    path("decrease/<slug>", decrease_quantity_view, name="decrease_url"),
    path("clear/", erase_cart_view, name="clear_cart_url" )
]
