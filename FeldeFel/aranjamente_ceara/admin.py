from django.contrib import admin
from .models import WaxArrangement

# Register your models here.

# admin.site.register(WaxArrangement) # ----> old fashion


@admin.register(WaxArrangement)
class WaxArrangementModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "price")
    search_fields = ("name", "description", "slug", "price")
    prepopulated_fields = {"slug":("name",)}
