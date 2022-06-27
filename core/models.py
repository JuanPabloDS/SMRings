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

class Anel(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')
    imagem = StdImageField('imagem', upload_to=get_file_path, variations={'thumb': (124, 124), 'thumb-index': (150, 150)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self) -> str:
        return self.nome
    
def anel_pre_save(signal, instance, sender, **kwargs):  #Função que vai ser executada ao cadastrar o ANEL
    instance.slug = slugify(instance.nome)                
                                                           
signals.pre_save.connect(anel_pre_save, sender=Anel)