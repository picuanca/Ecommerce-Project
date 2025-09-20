from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Client
# from .models import Item

# Create your views here.

#####   VARIANTA 2   ####

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # loghează userul
            return redirect("home:home")  # îl trimite acasă
        else:
            return render(request, "accounts/login.html", {"error": "Date incorecte!"})

    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)  # deloghează userul
    return redirect("home:home")


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")        
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        postal_code = request.POST.get("postal_code")

        ## verificare ##
        if not first_name or not last_name or not email or not password:
            return render(request, "accounts/register.html", {"error": "Toate câmpurile sunt        obligatorii!"})

        if password != confirm_password:
            return render(request, "accounts/register.html", {"error": "Parolele nu coincid!"})

        if User.objects.filter(username=email).exists():
            return render(request, "accounts/register.html", {"error": "Utilizatorul există deja!"})

        ## crearea user-ului ##
        user = User.objects.create_user(
            username=email, 
            email=email, 
            password=password, 
            first_name=first_name, 
            last_name=last_name
        )

        user.is_staff = False
        user.is_superuser = False
        user.save()

        ## creare cont si profil client ##
        Client.objects.create(
            user=user,
            phone=phone,
            address=address,
            city=city,
            postal_code=postal_code
            )

        
        ### logare directa a userului dupa inregistrare ##
        login(request, user) 
        return redirect("home:home")

    return render(request, "accounts/register.html")

from django.contrib.auth.decorators import login_required
from orders.models import Order,Return

@login_required
def profile_view(request):
    try:
        client = request.user.client
    except Client.DoesNotExist:
        client = None
    
    orders = Order.objects.filter(client=client) if client else []
    returns = Return.objects.filter(order_item__order__client=client) if client else []

    context = {
        "user": request.user,
        "client": client,
        "orders": orders,
        "returns": returns,
    }
    return render(request, "accounts/profile.html", context)
    # if not request.user.is_authenticated:
    #     return redirect("accounts:login")

    # print("Este utilizatorul logat?:", request.user)
    # return render(request, "accounts/profile.html", {"user": request.user})

def only_logged_users_view(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    return render(request, "accounts/only_logged_users.html")




####   VARIANTA 1   ######

# def profile_view(request):
#     context = {}

#     if not request.user.is_authenticated:
#         return redirect("login")


#     print("Este utilizatorul logat?:", request.user)

#     return render(request, "profile.html", context)

# from django.contrib.auth.decorators import login_required

# @login_required
# def only_logged_users_view(request):
#     return render(request, "only_logged_users.html")



# def register_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")

#         if password != confirm_password:
#             messages.error(request, "Parola nu coincide")
#             return redirect("accounts:register")
        
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Numele de utilizator există deja.")
#             return redirect("accounts:register")
        
#         user = User.objects.create_user(username=username, email=email, password=password)
#         messages.success(request, "Cont creat cu succes! Te poți autentifica.")
#         return redirect("accounts:login")
    
#     return render(request, "accounts.register.html")


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, "Autentificat cu succes!")
#             return redirect("home:home")
#         else:
#             messages.error(request, "Date de autentificare incorecte.")
#             return redirect("accounts:login")

#     return render(request, "accounts/login.html")


# def logout_view(request):
#     logout(request)
#     messages.success(request, "Te-ai deconectat.")
#     return redirect("home:home")


