from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class CarrinhoView(TemplateView):
    template_name: str = 'carrinho.html'  # Nome do Template


def delete_cart(request, pk):
    """
    Apaga os itens do carrinho ao clicar 
    no icone de deletar
    """

    direct = request.session['redirect'] # Variavel que armazena os dados do redirect

    if pk:
        carrinho = request.session['carrinho']
        carrinho.pop(str(pk))  # Remove o item do carrinho
        print(carrinho)
        request.session['carrinho'] = carrinho  # Salva os novos dados do carrinho na session
        return redirect(str(direct))
        



    return render(request, 'carrinho.html') 
