"""Models module"""

from colorfield.fields import ColorField
from django.db import models
from django.db.models import fields
from django.db.models.functions import Concat


class Projeto(models.Model):
    """
    Modelo de projeto
    """

    titulo = models.CharField(max_length=255, null=False)
    objetivo = models.TextField(null=False)
    descricao = models.TextField(null=False)
    data_criacao = models.DateField(null=False)
    data_conclusao = models.DateField(blank=True, null=True)
    valor_solicitado = models.DecimalField(max_digits=11, decimal_places=2)
    cancelado = models.BooleanField(default=False)
    area = models.ForeignKey(
        "Area",
        on_delete=models.SET_NULL,
        related_name="projeto_set",
        null=True,
        blank=True,
    )
    subarea = models.ManyToManyField(
        "SubArea",
        related_name="projeto_set",
        blank=True
    )
    agencias_fomento = models.ManyToManyField(
        'AgenciaFomento',
        related_name='projeto_set',
        blank=True
    )

    @property
    def status(self):
        """
        Retorna o status do projeto
        """
        if self.cancelado:
            return "CANCELADO"
        if self.data_conclusao:
            return "CONCLUIDO"
        return "EM_ANDAMENTO"

    @property
    def valor_total_arrecadado(self):
        """
        Retorna o valor total arrecadado
        """
        total = 0
        for valor in self.valores_arrecadados.all():
            total += valor.valor
        return total

    @property
    def coordenador(self):
        """
        Retorna o coordenador do projeto
        """
        for pesquisador_projeto in self.pesquisadores.all():
            if pesquisador_projeto.cargo == "COORDENADOR":
                return pesquisador_projeto.pesquisador
        return None

    def __str__(self):
        return str(self.titulo)


class Area(models.Model):
    """
    Modelo de área do conhecimento
    """

    nome = models.CharField(max_length=255, null=False)
    cor = ColorField(default="#FF0000")

    def __str__(self):
        return str(self.nome)


class SubArea(models.Model):
    """
    Modelo de subárea do conhecimento
    """

    nome = models.CharField(max_length=255, null=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="subarea_set")

    def __str__(self):
        return str(self.nome)


class Pesquisador(models.Model):
    """
    Modelo de pesquisador
    """

    nome = models.CharField(max_length=255, null=False)
    sobrenome = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    data_nascimento = models.DateField(null=False)
    foto_perfil = models.CharField(max_length=255, null=True)
    curriculo_lattes = models.CharField(max_length=255, null=True)
    full_name = fields.generated.GeneratedField(
        expression=Concat("nome", models.Value(" "), "sobrenome"),
        output_field=models.CharField(max_length=510),
        db_persist=True,
    )

    @property
    def producoes_academicas(self):
        """
        Retorna as produções acadêmicas do pesquisador
        """
        return ProducaoAcademica.objects.filter(projeto__pesquisadores=self)

    @property
    def numero_projetos(self):
        """
        Retorna o número de projetos do pesquisador
        """
        return self.projetos_set.count()

    @property
    def numero_producoes(self):
        """
        Retorna o número de produções acadêmicas do pesquisador
        """
        return self.producoes_academicas.count()

    def __str__(self):
        return str(self.nome)


class PesquisadorProjeto(models.Model):
    """
    Modelo de relação entre pesquisador e projeto
    """

    pesquisador = models.ForeignKey(
        Pesquisador, on_delete=models.CASCADE, related_name="projetos"
    )
    projeto = models.ForeignKey(
        Projeto, on_delete=models.CASCADE, related_name="pesquisadores"
    )
    cargo = models.CharField(max_length=255, null=False)
    horas = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.pesquisador} - {self.projeto}"


class AgenciaFomento(models.Model):
    """
    Modelo de agência de fomento
    """

    nome = models.CharField(max_length=255, null=False)
    sigla = models.CharField(max_length=10, null=False)

    def __str__(self):
        return f"{self.nome} - {self.sigla}"


class ValorArrecadado(models.Model):
    """
    Modelo de valor arrecadado
    """

    valor = models.DecimalField(max_digits=11, decimal_places=2)
    descricao = models.TextField(null=False)
    data = models.DateField(null=False)
    projeto = models.ForeignKey(
        "Projeto", on_delete=models.CASCADE, related_name="valores_arrecadados"
    )

    def __str__(self):
        return f"{self.valor} - {self.data} - {self.descricao}"


class ProducaoAcademica(models.Model):
    """
    Modelo de produção acadêmica
    """

    titulo = models.CharField(max_length=255, null=False)
    descricao = models.TextField(null=False)
    tipo = models.CharField(max_length=255, null=False)
    projeto = models.ForeignKey(
        "Projeto", on_delete=models.CASCADE, related_name="producoes_academicas"
    )

    def __str__(self):
        return f"{self.titulo} - {self.projeto}"
