from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import AnelModelForm

from .models import Anel

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

def cadastro(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = AnelModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                messages.success(request, 'Anel salvo com sucesso!')
                form = AnelModelForm()

            else:
                messages.error(request, 'Erro ao salvar anel')
        else:
            form = AnelModelForm()


        context = {
            'form': form
        }
    
        return render(request, 'cadastro.html', context)
    else:
        return redirect('index')