from django.contrib import admin

from .models import Anel

@admin.register(Anel)
class AnelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')
    