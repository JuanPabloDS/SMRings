from atexit import register
from django.contrib import admin


from .models import Carrinho, CarrinhoAneis


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'finalizado', 'criado', 'modificado')


@admin.register(CarrinhoAneis)
class CarrinhoAneisAdmin(admin.ModelAdmin):
    list_display = ('carrinho_id', 'anel_id')