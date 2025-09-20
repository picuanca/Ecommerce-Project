from django.urls import path
from .views import register_view
from .views import login_view
from .views import logout_view
from .views import profile_view
 

app_name = "accounts"

urlpatterns = [

	path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),   
    
]
