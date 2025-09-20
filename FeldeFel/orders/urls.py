from django.urls import path
# from .views import orders_view

from .views import checkout_view
from .views import order_success_view

app_name = "orders"

urlpatterns = [
	# path("orders", orders_view),
    path("checkout/", checkout_view, name="checkout"),   # Pagina de plasare a comenzii
    path("success/", order_success_view, name="order_success"),  # Pagina de confirmare
]
