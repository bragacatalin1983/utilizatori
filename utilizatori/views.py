from django.shortcuts import render, get_object_or_404, redirect
from .models import Utilizatori
from django.db.models import Q


def home(request):

    return render(request, 'home.html')


def utilizatori(request):
    utilizatori = Utilizatori.objects.order_by('nume')

    context = {
        'utilizatori': utilizatori,
    }

    return render(request, 'utilizatori.html', context)


def om(request, pk_id):
    om = get_object_or_404(Utilizatori, pk=pk_id)
    return render(request, 'om.html', {'om': om})


def search(request):
    template = 'home.html'
    query = request.GET.get('q')
    results = Utilizatori.objects.filter(
        Q(nume__icontains=query) | Q(cnp__icontains=query))
    context = {
        'items': results}

    return render(request, template, context)
