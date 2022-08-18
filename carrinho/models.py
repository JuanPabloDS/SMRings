from django.db import models
from django.forms import CharField
from usuarios.models import Clientes
from core.models import Anel, Base

class Carrinho(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('data de Atualização', auto_now=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.SET('Anonymous'))
    finalizado = models.BooleanField('Finalizado?', default=False)



    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'

    def __str__(self) -> str:
        return f'Carrinho: {self.cliente} Nº {self.id}'
    

class CarrinhoAneis(models.Model):
    carrinho_id = models.ForeignKey(Carrinho, on_delete=models.SET('0'))
    anel_id = models.ForeignKey(Anel, on_delete=models.SET('0'))
    quantidade = models.IntegerField('Quantidade')
    tamanho = models.IntegerField('Tamanho')

    def register(self):
        self.save()


    class Meta:
        verbose_name = 'Anel Vendido'
        verbose_name_plural = 'Aneis Vendidos'


