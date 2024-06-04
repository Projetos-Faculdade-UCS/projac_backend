"""Models module"""

from colorfield.fields import ColorField
from django.db import models

gender_choices = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
    ('P', 'Prefiro não informar'),
)


class Projeto(models.Model):
    """
        Modelo de projeto
    """

    titulo = models.CharField(max_length=255, null=False)
    objetivo = models.TextField(null=False)
    descricao = models.TextField(null=False)
    data_criacao = models.DateField(null=False)
    data_conclusao = models.DateField(null=True)
    valor_solicitado = models.DecimalField(max_digits=11, decimal_places=2)
    cancelado = models.BooleanField(default=False)
    area = models.ForeignKey(
        'Area',
        on_delete=models.SET_NULL,
        related_name='projeto_set',
        null=True,
        blank=True
    )
    subarea = models.ManyToManyField(
        'SubArea',
        related_name='projeto_set',
        blank=True
    )
    pesquisadores = models.ManyToManyField(
        'Pesquisador',
        through='PesquisadorProjeto',
        related_name='projeto_set',
        blank=True
    )

    def __str__(self):
        return str(self.titulo)


class Area(models.Model):
    """
        Modelo de área do conhecimento
    """
    nome = models.CharField(max_length=255, null=False)
    cor = ColorField(default='#FF0000')

    def __str__(self):
        return str(self.nome)


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
        return str(self.nome)


class Pesquisador(models.Model):
    """
        Modelo de pesquisador
    """
    nome = models.CharField(max_length=255, null=False)
    sobrenome = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    genero = models.CharField(max_length=1, choices=gender_choices, default='P', null=False)
    telefone = models.CharField(max_length=15, null=False)
    data_nascimento = models.DateField(null=False)
    foto_perfil = models.CharField(max_length=255, null=True)

    @property
    def full_name(self):
        """
            Retorna o nome completo do pesquisador
        """
        return f'{self.nome} {self.sobrenome}'

    def __str__(self):
        return str(self.nome)


class PesquisadorProjeto(models.Model):
    """
        Modelo de relação entre pesquisador e projeto
    """
    pesquisador = models.ForeignKey(
        Pesquisador,
        on_delete=models.CASCADE,
        related_name='pesquisadorprojeto_set'
    )

    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='pesquisadorprojeto_set'
    )

    cargo = models.CharField(max_length=255, null=False)

    horas = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.pesquisador} - {self.projeto}'
