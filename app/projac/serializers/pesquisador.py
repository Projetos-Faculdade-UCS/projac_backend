"""pesquisador serializers module"""

from projac.models import Pesquisador, PesquisadorProjeto
from rest_framework import serializers


class PesquisadorListInProjectDetail(serializers.ModelSerializer):
    """Used to serialize the list of pesquisadores in a project detail"""

    id = serializers.IntegerField(source="pesquisador.id")
    nome = serializers.CharField(source="pesquisador.nome")
    sobrenome = serializers.CharField(source="pesquisador.sobrenome")
    foto_perfil = serializers.CharField(source="pesquisador.foto_perfil")

    class Meta:
        """Meta class"""
        model = PesquisadorProjeto
        fields = [
            "id",
            "nome",
            "sobrenome",
            "foto_perfil",
            "cargo",
            "horas",
        ]


class PesquisadorProjectListSerializer(serializers.ModelSerializer):
    """Used to serialize a pesquisador(coordenador) in a project list"""

    class Meta:
        """Meta class"""

        model = Pesquisador
        fields = ['id', 'nome', 'sobrenome']
