from django.shortcuts import render
from apps.pokemon.models import Pokemon
from django.db.models import Q

# Create your views here.
def pokemon_list(request):
    # data_context = [
    #     {'nombre': 'Luis Pardo',
    #      'edad': 24,
    #      'pais': 'Peru'}
    # ]
    #data_context = Pokemon.objects.all()
    query = Q(tipo='fuego')
    data_context = Pokemon.objects.filter(query)
    return render(request, 'pokemon/templates/pokemon/pokemon_list.html', context={'data': data_context})


