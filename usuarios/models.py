from django.db import models


class Clientes(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
  
    # to save the data
    def register(self):
        self.save()
  
    @staticmethod
    def get_cliente_by_email(email):
        try:
            return Clientes.objects.get(email=email)
        except:
            return False
  
    def isExists(self):
        if Clientes.objects.filter(email=self.email):
            return True
  
        return False

