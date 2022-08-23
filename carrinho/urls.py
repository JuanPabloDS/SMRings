from ast import pattern
from django.urls import path
from .views import CarrinhoView, delete_cart


urlpatterns = [
    path('carrinho/<int:pk>', delete_cart, name='carrinho'),

]