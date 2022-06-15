from django.shortcuts import render
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

    if str(request.method) == 'POST':
        form = AnelModelForm(request.POST, request.FILES)
        if form.is_valid():
            ane = form.save(commit=False)

            print(f'Nome: {ane.nome}')
            print(f'preco: {ane.preco}')
            print(f'estoque: {ane.estoque}')
            print(f'imagem: {ane.imagem}')

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
