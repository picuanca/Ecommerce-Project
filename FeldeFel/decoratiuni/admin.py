from django.contrib import admin
from .models import OnyxDecoration,ResinDecoration

# Register your models here.

# admin.site.register(OnyxDecoration)
# admin.site.register(ResinDecoration)

@admin.register(OnyxDecoration)
class OnyxDecorationModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "price")
    search_fields = ("name", "description", "slug", "price")
    prepopulated_fields = {"slug":("name",)}


@admin.register(ResinDecoration)
class ResinDecorationModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "price")
    search_fields = ("name", "description", "slug", "price")
    prepopulated_fields = {"slug":("name",)} 
