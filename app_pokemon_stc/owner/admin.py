from django.contrib import admin

from owner.models import Owner


# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass