from django.shortcuts import render, redirect
from aranjamente_flori.models import NaturalFlower, ArtificialFlower
from aranjamente_ceara.models import WaxArrangement
from decoratiuni.models import OnyxDecoration, ResinDecoration



# Create your views here.

MODEL_MAP = {
    'natural': NaturalFlower,
    'artificial': ArtificialFlower,
    'wax': WaxArrangement,
    'onyx': OnyxDecoration,
    'resin': ResinDecoration,
}



def cart_view(request):
    cart = request.session.get("cart", {})
    total = 0
    updated_cart = {}

    for slug, item in cart.items():
        subtotal = round(item["price"] * item["quantity"], 2)
        item["subtotal"] = subtotal
        total += subtotal
        updated_cart[slug] = item
    # total = sum(item["subtotal"] for item in cart.values())
    # total = sum(item["price"] * item["quantity"] for item in cart.values())
    context = {
        "cart": cart,
        "total": round(total, 2)
    }
    return render(request, "cart/cart.html", context)


def add_to_cart_view(request, slug):
    for model_class in MODEL_MAP.values():
        try:
            product = model_class.objects.get(slug=slug)
            break
        except model_class.DoesNotExist:
            continue
    else:
        return redirect("cart:cart_url")  # Dacă nu găsește produsul

    cart = request.session.get("cart", {})

    try:
        quantity = int(request.POST.get("quantity", 1))
    except ValueError:
        quantity = 1

    if slug in cart:
        cart[slug]["quantity"] += quantity
    else:
        cart[slug] = {
            "name": product.name,
            "price": float(product.price),
            "quantity": quantity,
            "slug": slug,
            "image": product.image.url,
            # "image_url": product.image.url,
            # "image_url": product.image,
        }

    cart[slug]["subtotal"] = round(cart[slug]["price"] * cart[slug]["quantity"], 2)
    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart:cart_url")


def erase_cart_view(request):
    request.session["cart"] = {}
    request.session.modified = True
    return redirect("cart:cart_url")


def increase_quantity_view(request, slug):
    cart = request.session.get("cart", {})
    if slug in cart:
        cart[slug]["quantity"] += 1
        request.session.modified = True
    return redirect("cart:cart_url")


def decrease_quantity_view(request, slug):
    cart = request.session.get("cart", {})
    if slug in cart:
        cart[slug]["quantity"] -= 1
        if cart[slug]["quantity"] <= 0:
            del cart[slug]
        else:
            cart[slug]["subtotal"] = round(cart[slug]["price"] * cart[slug]["quantity"], 2)
        request.session.modified = True
    return redirect("cart:cart_url")