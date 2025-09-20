from django.contrib import admin
from .models import Order
from .models import OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product_name", "product_price", "quantity", "subtotal")

    def subtotal(self, obj):
        return obj.get_subtotal()
    subtotal.short_description = "Subtotal"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "phone", "city", "total", "created", "paid")
    list_filter = ("paid", "created", "updated")
    search_fields = ("first_name", "last_name", "email", "phone")
    inlines = [OrderItemInline]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = "Client"

    def total(self, obj):
        return obj.get_total()
    total.short_description = "Total comanda"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product_name", "product_price", "quantity", "subtotal")

    def subtotal(self, obj):
        return obj.get_subtotal()
    subtotal.short_description = "Subtotal"
