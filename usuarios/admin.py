from django.contrib import admin

from .models import Clientes


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'email')
