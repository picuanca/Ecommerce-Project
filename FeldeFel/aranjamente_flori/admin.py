from django.contrib import admin
from .models import NaturalFlower,ArtificialFlower

# Register your models here.

# admin.site.register(NaturalFlower)
# admin.site.register(ArtificialFlower)

@admin.register(NaturalFlower)
class NaturalFlowerModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "price")
    search_fields = ("name", "description", "slug", "price")
    prepopulated_fields = {"slug":("name",)}


@admin.register(ArtificialFlower)
class ArtificialFlowerModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "price")
    search_fields = ("name", "description", "slug", "price")
    prepopulated_fields = {"slug":("name",)}
