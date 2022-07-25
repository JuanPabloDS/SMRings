from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class CarrinhoView(TemplateView):
    template_name: str = 'carrinho.html'


def logout(request, pk):
    
    red = request.session['redirect']

    print(pk)
    if pk:
        carrinho = request.session['carrinho']
        carrinho.pop(str(pk))
        print(carrinho)
        request.session['carrinho'] = carrinho
        return redirect(str(red))
        



    return render(request, 'carrinho.html')
