from django.shortcuts import render, redirect

from owner.models import Owner
from owner.forms import OwnerForm
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core import serializers as ssr
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView

from owner.serializers import OwnerSerializer

# Create your views here.
def owner_list(request):
    # data_context = [
    #     {'nombre': 'Luis Pardo',
    #      'edad': 24,
    #      'pais': 'Peru'}
    # ]
    # data_context = Owner.objects.all()
    query = Q(pais='Peru')
    data_context = Owner.objects.filter(query)

    return render(request, 'owner/owner_list.html', context={'data': data_context})

def owner_details(request):
    data_context=Owner.objects.all()
    return render(request, 'owner/owner_details.html',context={'data':data_context})

def owner_search(request):
    query = request.GET.get('q', '')
    results = (
        Q(nombre__icontains=query) | Q(pais__icontains=query)
    )
    data_context = Owner.objects.filter(results)

    return render(request, 'owner/owner_search.html', context={'data': data_context, 'query': query})

def owner_delete(request,id_owner):
    owner = Owner.objects.get(id=id_owner)
    owner.delete()
    return render(request,'owner/owner_confirm_delete.html',context={'owner':id_owner})

def owner_edit(request,id_owner):
    owner = Owner.objects.get(id=id_owner)
    form = OwnerForm(initial={'nombre':owner.nombre,'edad':owner.edad,'pais':owner.pais,'habilitado':owner.habilitado})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_details')

    return render(request,'owner/owner_edit.html',{'form':form})

class OwnerList(ListView):
    model = Owner
    template_name = 'owner/owner_list_vbc.html'

class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_create.html'
    success_url = reverse_lazy('owner_list_vbc')

class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_update_vbc.html'
    success_url = reverse_lazy('owner_details')

class OwnerDelete(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_vbc')
    template_name = 'owner/owner_confirm_delete.html'

def ListOwnerSerializer(request):
    list_owner = ssr.serialize('json',Owner.objects.all(),fields = ['nombre','pais','edad','dni'])
    return HttpResponse(list_owner,content_type='application/json')

@api_view(['GET'])
def owner_api_view(request):
    if request.method == 'GET':
        print('Ingresó a GET')
        queryset = Owner.objects.all()
        serializers_class = OwnerSerializer(queryset, many=True)

    return Response(serializers_class.data)

@api_view(['PUT'])
def owner_api_update(generics.UpdateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    lookup_field = 'id'



