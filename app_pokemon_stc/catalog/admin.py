from django.contrib import admin

from catalog.models import Catalog

# Register your models here.
@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    pass