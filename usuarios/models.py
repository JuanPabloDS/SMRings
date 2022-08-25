from urllib import request
from django.db import models


class Clientes(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
  
    # Salvar os dados no banco
    def register(self):
        self.save()
  
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    @staticmethod
    def get_cliente_by_email(email):
        """Busca o email cadastrado dentro do banco"""
        try:
            return Clientes.objects.get(email=email)
        except:
            return False
  
    def isExists(self):
        """Verifica se o email existe no banco"""
        if Clientes.objects.filter(email=self.email):
            return True
  
        return False
    
    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.nome} {self.sobrenome}'



