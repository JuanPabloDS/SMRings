from django.shortcuts import render

from core.models import Anel

def index(request):
    aneis = Anel.objects.all()

    context = {
        'aneis': aneis
    }


    return render(request, 'index.html', context)


def aneis(request, pk):
    anel = Anel.objects.get(id=pk) 

    context = {
        'anel': anel
    }



    return render(request, 'aneis.html', context)
