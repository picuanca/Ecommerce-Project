from django.shortcuts import render, redirect
from .models import Order, OrderItem
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import Client

# Create your views here.

def checkout_view(request):
    cart = request.session.get("cart", {})

    if request.method == "POST":
        if not cart:
            messages.error(request, "Coșul este gol")
            return redirect("cart:cart_url")

        # Obține clientul dacă e logat
        client_instance = None
        if request.user.is_authenticated:
            try:
                client_instance = request.user.client
            except Client.DoesNotExist:
                client_instance = None

        # Creează comanda
        order = Order.objects.create(
            client=client_instance,
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            postal_code=request.POST.get("postal_code")
        )

        # Adaugă produsele
        for item in cart.values():
            OrderItem.objects.create(
                order=order,
                product_name=item["name"],
                product_price=item["price"],
                quantity=item["quantity"],
                product_image=item.get("image"),
            )

        # Golire cos
        request.session["cart"] = {}

        # Opțional: trimitere mail
        try:
            total = order.get_total()
            send_mail(
                subject=f"Confirmare comandă #{order.id}",
                message=(
                    f"Salut {order.first_name},\n\n"
                    f"Îți mulțumim pentru comanda ta!\n\n"
                    f"Număr comandă: {order.id}\n"
                    f"Total: {total} RON\n\n"
                    f"Produse comandate:\n" +
                    "\n".join([f"- {i.product_name} × {i.quantity} = {i.subtotal} RON"
                               for i in order.items.all()]) +
                    f"\n\nComanda va fi livrată la adresa: {order.address}, {order.city}."
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[order.email],
                fail_silently=True,
            )
        except:
            pass

        messages.success(request, "Comanda a fost plasată cu succes!")
        return redirect("orders:order_success")

    # GET: afișare checkout
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    client_data = {}
    if request.user.is_authenticated:
        try:
            client = request.user.client
            client_data = {
                "first_name": client.user.first_name,
                "last_name": client.user.last_name,
                "email": client.user.email,
                "phone": client.phone,
                "address": client.address,
            }
        except Client.DoesNotExist:
            pass

    context = {
        'cart': cart,
        'total': total,
        'client_data': client_data
    }
    return render(request, "orders/checkout.html", context)


def order_success_view(request):
	return render(request, "orders/order_success.html")