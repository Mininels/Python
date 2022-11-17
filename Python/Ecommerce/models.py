from django.db import models


"""
Produto:
    nome - Char
    descricao_curta - text
    descricao_longa - text
    slug - Slug
    Imagem - Image
    preco Marketing - Float
    preco_marketing_promocional - Float
    Tipo - Choices 
        ('V', 'Variavel'),
        ('S', 'Simples'),

"""
class Produto(models.Model):
    nome                            = models.CharField(max_lenght=255)
    descricao_curta                 = models.TextField(max_lenght=255)
    descricao_longa                 = models.TextField()
    Imagem                          = models.models.ImageField(upload_to='produto_imagens/%Y/%m', blank=True, null=True )
    slug                            = models.SlugField(unique=True)
    preco                           = models.FloatField(default=0)
    preco_marketing                 = models.FloatField(default=0)
    preco_marketing_promocional     = models.FloatField()
    tipo                            = models.charfield(default='V',
                                                       max_lengt=1,
                                                       choices=(
                                                            ('V', 'Variavel'),
                                                            ('S', 'Simples'),
                                                         )
                                                    )
"""

Varoacao:
    nome - char 
    produto - FK produto
    preco - Float
    preco_promocional - Float
    estoque - int



"""