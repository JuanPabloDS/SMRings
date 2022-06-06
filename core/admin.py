from django.contrib import admin

from .models import Anel

class AnelAdmin(admin.ModelAdmin) :
    list_display = ('nome', 'preco', 'estoque')

admin.site.register(Anel, AnelAdmin)