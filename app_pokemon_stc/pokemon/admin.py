from django.contrib import admin

from pokemon.models import Pokemon


# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    fields = ('nombre','tipo','numero') # no mostrar generacion para crear o editar
    search_fields = ('nombre',)  # agrega barra de búsqueda por el nombre
    list_display = ('nombre','generacion','tipo') # campos que se mostrarán en admin