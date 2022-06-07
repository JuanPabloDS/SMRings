from django.db import models

class Anel(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')
    imagem = models.CharField('Imagem', max_length=150)

    def __str__(self) -> str:
        return self.nome