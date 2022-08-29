from django.contrib import admin

from .models import Anel, Tamanho


@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('tamanho',)


@admin.register(Anel)
class AnelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'caminho', 'criado', 'modificado', 'ativo', 'get_tamanhos')

    def get_tamanhos(self, obj):
        """
        Função para mostrar os tamanhos dos aneis
        """
        lista = [num for num in obj.tamanho.all()]
        dados = ([str(num) for num in lista])

        
        return ', '.join([m for m in dados])

    get_tamanhos.short_description = 'Tamnhos'


