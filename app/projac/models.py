from typing import Any
from colorfield.fields import ColorField
from django.db import models


class Projeto(models.Model):
    '''
        Modelo de projeto
    '''

    titulo = models.CharField(max_length=255, null=False)
    objetivo = models.TextField(null=False)
    data_criacao = models.DateTimeField(null=False)
    data_conclusao = models.DateTimeField(null=True)
    valor_solicitado = models.DecimalField(max_digits=11, decimal_places=2)
    descricao = models.TextField(null=False)
    info_extras = models.TextField(null=True)
    cancelado = models.BooleanField(default=False)

    area = models.ForeignKey(
        'Area',
        on_delete=models.SET_NULL,
        related_name='projeto_set',
        null=True,
        blank=False
    )

    subarea = models.ManyToManyField(
        'SubArea',
        related_name='projeto_set',
        blank=False
    )

    def __str__(self):
        return self.titulo

        

class Area(models.Model):  
    """
        Modelo de área do conhecimento
    """
    nome = models.CharField(max_length=255, null=False)
    cor = ColorField(default='#FF0000') 

    def __str__(self):
        return self.nome

class SubArea(models.Model):
    """
        Modelo de subárea do conhecimento
    """
    nome = models.CharField(max_length=255, null=False)
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        related_name='subarea_set'
    )

    def __str__(self):
        return self.nome
    

