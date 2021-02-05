from django.shortcuts import render, get_object_or_404, redirect
from .models import Utilizatori


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        user_name = request.POST['username']

        qs = Utilizatori.objects.filter(nume__icontains="user_name")
        if qs == True:
            return render(request, 'home.html', {'rezultat': 'DA'})
        else:
            return render(request, 'home.html', {'rezultat': 'Nu exista in baza de date'})


def utilizatori(request):
    utilizatori = Utilizatori.objects.order_by('-date')

    context = {
        'utilizatori': utilizatori,
    }

    return render(request, 'utilizatori.html', context)


def om(request, pk_id):
    om = get_object_or_404(Utilizatori, pk=pk_id)
    return render(request, 'om.html', {'om': om})
