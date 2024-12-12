from django.shortcuts import render, redirect

from apps.owner.models import Owner
from apps.owner.forms import OwnerForm
from django.db.models import Q

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.core import serializers as ssr
from apps.owner.serializers import OwnerSerializer
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
    return render(request, 'owner/owner_details.html', context={'data':data_context})

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
    return render(request, 'owner/owner_confirm_delete.html', context={'owner':id_owner})

def owner_edit(request,id_owner):
    owner = Owner.objects.get(id=id_owner)
    form = OwnerForm(initial={'nombre':owner.nombre,'edad':owner.edad,'pais':owner.pais,'habilitado':owner.habilitado})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_details')

    return render(request, 'owner/owner_edit.html', {'form':form})

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

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def owner_api_view(request):
    if request.method == 'GET':
        print('Ingresó a GET')
        queryset = Owner.objects.all()
        serializers_class = OwnerSerializer(queryset, many=True)
        return Response(serializers_class.data)

    elif request.method == 'POST':
        print('DATA OWNER: {}',format(request.data))
        serializers_class = OwnerSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data)
        return Response(serializers_class.errors)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def owner_details_view(request,pk):
    owner = Owner.objects.get(id=pk)
    if owner:
        if request.method == 'GET':
            serializer_class = OwnerSerializer(owner)
            return Response(serializer_class.data)
        elif request.method == 'PUT':
            serializer_class = OwnerSerializer(owner,data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data)
            return Response(serializer_class.errors)
        elif request.method == 'DELETE':
            owner.delete()
            return Response('Owner eliminado satisfactoriamente.')

