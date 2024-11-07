from django.contrib import admin

from pokemon.models import Pokemon


# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass