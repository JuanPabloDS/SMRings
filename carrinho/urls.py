from ast import pattern
from django.urls import path
from .views import CarrinhoView


urlpatterns = [
    path('carrinho', CarrinhoView.as_view(), name='carrinho'),

]