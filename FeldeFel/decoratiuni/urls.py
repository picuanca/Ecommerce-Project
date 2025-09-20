from django.urls import path
from .views import resin_decorations_view
from .views import onyx_decorations_view
from .views import onyx_decorations_details_view
from .views import resin_decorations_details_view

app_name = "decoratiuni"

urlpatterns = [
    path("onyx", onyx_decorations_view, name="decoratiuni_onyx"),
    path("rasina", resin_decorations_view, name="decoratiuni_rasina"),
    path("onyx/<slug:slug>/", onyx_decorations_details_view, name="detalii_onyx"),
    path("rasina/<slug:slug>/", resin_decorations_details_view, name="detalii_rasina")
]
