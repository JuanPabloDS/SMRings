import uuid
from distutils.command.upload import upload
from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals

def get_file_path(_instance, filename):
    """ Função para gerar nomes aleátorios quando for salvar um
    arquivo de imagem"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

from django.template.defaultfilters import slugify # Pega o nome do produto e passa na URL

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Tamanho(models.Model):
    tamanho = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'

    def __str__(self) -> str:
        return self.tamanho


class Anel(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    tamanho = models.ManyToManyField(Tamanho)
    estoque = models.IntegerField('Quantidade em estoque')
    imagem = StdImageField('imagem', upload_to=get_file_path, variations={'thumb': (124, 124), 'thumb-index': (150, 150)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self) -> str:
        return str(self.nome)

    def get_key(val, session):
        """Função para buscar Id dos aneis dentro da session carrinho"""
        for key, value in session.items():
            if val == key:
                return True
    
        return False

    def real_br_money(my_value):
        """Função para converter dolar em real"""
        a = '{:,.2f}'.format(float(my_value))
        b = a.replace(',','v')
        c = b.replace('.',',')
        return c.replace('v','.')

    def dolar_money(my_value):
        """Função para converter real em dolar"""
        a = my_value.replace('.','')
        b = a.replace(',', '.')
        return float(b)