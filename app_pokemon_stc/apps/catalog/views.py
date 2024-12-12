from django.shortcuts import render
from apps.catalog.models import Catalog

# Create your views here.
def catalog_list(request):
    # data_context=[
    #     {'nombre':'Luis Pardo',
    #     'edad':24,
    #     'pais':'Peru'}
    # ]
    data_context = Catalog.objects.all()
    return render(request, 'catalog/catalog_list.html', context={'data':data_context})