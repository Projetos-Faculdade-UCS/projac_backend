"""pesquisador serializers module"""

from projac.models import Pesquisador, PesquisadorProjeto
from rest_framework import serializers
from .area_subarea import AreaSerializer
from .producao_academica import ProducaoAcademicaSerializer


class CoordenadorInProjectListSerializer(serializers.ModelSerializer):
    """Used to serialize a pesquisador(coordenador) in a project list"""

    class Meta:
        """Meta class"""

        model = Pesquisador
        fields = ["id", "nome", "sobrenome", "foto_perfil"]


class ProjectListInPesquisadorDetail(serializers.ModelSerializer):
    """Used to serialize the list of projetos in a pesquisador detail"""

    id = serializers.IntegerField(source="projeto.id")
    titulo = serializers.CharField(source="projeto.titulo")
    objetivo = serializers.CharField(source="projeto.objetivo")
    data_criacao = serializers.DateField(source="projeto.data_criacao")
    status = serializers.CharField(source="projeto.status")
    area = AreaSerializer(source="projeto.area")
    coordenador = CoordenadorInProjectListSerializer(source="projeto.coordenador")

    class Meta:
        """Meta class"""

        model = PesquisadorProjeto
        fields = [
            "id",
            "titulo",
            "objetivo",
            "data_criacao",
            "status",
            "horas",
            "area",
            "coordenador",
        ]


class PesquisadorListSerializer(serializers.ModelSerializer):
    """Used to serialize a pesquisador"""

    class Meta:
        """Meta class"""

        model = Pesquisador
        fields = [
            "id",
            "nome",
            "sobrenome",
            "email",
            "foto_perfil",
            "numero_projetos",
            "numero_producoes",     
        ]


class PesquisadorDetailSerializer(serializers.ModelSerializer):
    """Used to serialize a detail of an pesquisador"""

    projetos = ProjectListInPesquisadorDetail(source="projetos_set", many=True)
    producoes_academicas = ProducaoAcademicaSerializer(many=True)

    class Meta:
        """Meta class"""

        model = Pesquisador
        fields = [
            "id",
            "nome",
            "sobrenome",
            "email",
            "data_nascimento",
            "foto_perfil",
            "curriculo_lattes",
            "projetos",
            "producoes_academicas"
        ]
