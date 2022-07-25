from ast import pattern
from django.urls import path
from .views import CarrinhoView, logout


urlpatterns = [
    path('carrinho/<int:pk>', logout, name='carrinho'),

]