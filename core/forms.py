from django import forms

from .models import Anel

class AnelModelForm(forms.ModelForm):
    class Meta:
        model = Anel
        fields = ['nome', 'preco', 'estoque', 'imagem']
