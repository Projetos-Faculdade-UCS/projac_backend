"""projeto serializers module"""

from rest_framework import serializers
from projac.models import Area, PesquisadorProjeto, Projeto, SubArea, ProducaoAcademica, ValorArrecadado
from .pesquisador import CoordenadorInProjectListSerializer
from .producao_academica import ProducaoAcademicaSerializer
from .valor_arrecadado import ValorArrecadadoSerializer
from .agencia_fomento import AgenciaFomentoSerializer
from .area_subarea import AreaSerializer, SubAreaSerializer

class PesquisadorListInProjectDetail(serializers.ModelSerializer):
    """Used to serialize a list of pesquisadores in a project detail"""

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


class ProjetoDetailSerializer(serializers.ModelSerializer):
    """Projeto detail serializer"""

    area = AreaSerializer(read_only=True)
    area_id = serializers.PrimaryKeyRelatedField(
        queryset=Area.objects.all(), write_only=True, source="area"
    )
    subarea = SubAreaSerializer(read_only=True, many=True)
    subarea_ids = serializers.PrimaryKeyRelatedField(
        queryset=SubArea.objects.all(), write_only=True, source="subarea", many=True
    )
    producoes_academicas = ProducaoAcademicaSerializer(many=True, required=False)
    valores_arrecadados = ValorArrecadadoSerializer(many=True, required=False)
    pesquisadores = serializers.SerializerMethodField()
    agencias_fomento = AgenciaFomentoSerializer(many=True, read_only=True)

    class Meta:
        """Meta class"""

        model = Projeto
        fields = [
            "id",
            "titulo",
            "objetivo",
            "descricao",
            "data_criacao",
            "data_conclusao",
            "status",
            "area",
            "area_id",
            "subarea",
            "subarea_ids",
            "producoes_academicas",
            "valor_solicitado",
            "valor_total_arrecadado",
            "valores_arrecadados",
            "pesquisadores",
            "agencias_fomento",
        ]

    def create(self, validated_data):
        area = validated_data.pop("area")
        subareas = validated_data.pop("subarea")
        producoes_academicas = validated_data.pop("producoes_academicas", [])
        valores_arrecadados = validated_data.pop("valores_arrecadados", [])
        projeto = Projeto.objects.create(area=area, **validated_data)
        projeto.subarea.set(subareas)
        for producao_academica in producoes_academicas:
            ProducaoAcademica.objects.create(projeto=projeto, **producao_academica)
        for valor_arrecadado in valores_arrecadados:
            ValorArrecadado.objects.create(projeto=projeto, **valor_arrecadado)
        return projeto

    def get_pesquisadores(self, obj):
        """Get pesquisadores"""
        pesquisadores = []
        for pesquisador_projeto in obj.pesquisadores_set.all():
            pesquisadores.append(PesquisadorListInProjectDetail(pesquisador_projeto).data)
        return pesquisadores


class ProjetoListSerializer(serializers.ModelSerializer):
    """Projeto list serializer"""

    area = AreaSerializer(read_only=True)
    coordenador = CoordenadorInProjectListSerializer(read_only=True)

    class Meta:
        """Meta class"""

        model = Projeto
        fields = [
            "id",
            "titulo",
            "objetivo",
            "data_criacao",
            "status",
            "area",
            "coordenador",
        ]
