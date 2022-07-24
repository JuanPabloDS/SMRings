from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class CarrinhoView(TemplateView):
    template_name: str = 'carrinho.html'


def logout(request):
    request.session.clear()
    return redirect('/')
