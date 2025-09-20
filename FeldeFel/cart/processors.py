

def add_cart_to_context(request):
    cart = request.session.get("cart", {})
    total = 0

    for item in cart.values():
        total += round(item["price"] * item["quantity"], 2)

    return {
        "cart": cart,
        "cart_total": round(total, 2),
        "cart_count": sum(item["quantity"] for item in cart.values())
    }
