from django.db import models
from decimal import Decimal
from accounts.models import Client

# Create your models here.

class Order(models.Model):
    client = models.ForeignKey(
        Client, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="orders"
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Comanda {self.id} - {self.first_name} {self.last_name}"

    def get_total(self):
        """Calculează totalul comenzii pe baza produselor"""
        return sum((item.get_subtotal() for item in self.items.all()), Decimal('0'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    product_image = models.ImageField(upload_to="order_items/", blank=True, null=True)
    # product_image = models.URLFieldField(blank=True, null=True)

    def __str__(self):
        return f"{self.product_name} × {self.quantity}"

    def get_subtotal(self):
        """Calculează subtotalul acestui produs"""
        return self.product_price * self.quantity

    @property
    def subtotal(self):
        """Poate fi folosită direct în template-uri"""
        return self.get_subtotal()
    

class Return(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name="returns")
    reason = models.TextField(blank=True)  # motivul returului
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # dacă a fost aprobat returul

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Retur pentru {self.order_item.product_name} (Comanda #{self.order_item.order.id})"
