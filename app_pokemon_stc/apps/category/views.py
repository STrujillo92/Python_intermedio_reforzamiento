from django.shortcuts import render
from apps.category.models import Category

# Create your views here.
def category_list(request):
    # data_context = [
    #     {'nombre': 'Luis Pardo',
    #      'edad': 24,
    #      'pais': 'Peru'}
    # ]
    data_context = Category.objects.all()
    return render(request, 'category/category_list.html', context={'data': data_context})
