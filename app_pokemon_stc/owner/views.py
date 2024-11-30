from django.shortcuts import render, redirect
from owner.models import Owner
from owner.forms import OwnerForm
from django.db.models import Q

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

    return redirect('owner_details')

def owner_edit(request,id_owner):
    owner = Owner.objects.get(id=id_owner)
    form = OwnerForm(initial={'nombre':owner.nombre,'edad':owner.edad,'pais':owner.pais,'habilitado':owner.habilitado})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_details')

    return render(request,'owner/owner_edit.html',{'form':form})