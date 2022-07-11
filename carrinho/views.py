from django.shortcuts import render
from django.views.generic import TemplateView


class CarrinhoView(TemplateView):
    template_name: str = 'carrinho.html'


