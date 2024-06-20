"""projeto serializers module"""

from projac.models import (
    AgenciaFomento,
    Area,
    PesquisadorProjeto,
    ProducaoAcademica,
    Projeto,
    SubArea,
    ValorArrecadado,
)
from rest_framework import serializers

from .agencia_fomento import AgenciaFomentoSerializer
from .area_subarea import AreaSerializer, SubAreaSerializer
from .pesquisador import CoordenadorInProjectListSerializer
from .pesquisador_projeto import PesquisadorProjetoSerializer
from .producao_academica import ProducaoAcademicaSerializer
from .valor_arrecadado import ValorArrecadadoSerializer


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
        queryset=Area.objects.all(),
        write_only=True,
        source="area",
    )
    subarea = SubAreaSerializer(read_only=True, many=True)
    subarea_ids = serializers.PrimaryKeyRelatedField(
        queryset=SubArea.objects.all(),
        write_only=True,
        source="subarea",
        many=True,
    )
    producoes_academicas = ProducaoAcademicaSerializer(many=True, required=False)
    valores_arrecadados = ValorArrecadadoSerializer(many=True, required=False)
    pesquisadores = serializers.SerializerMethodField()
    pesquisador_projeto = PesquisadorProjetoSerializer(many=True, write_only=True)
    agencias_fomento = AgenciaFomentoSerializer(many=True, read_only=True)
    agencias_fomento_ids = serializers.PrimaryKeyRelatedField(
        queryset=AgenciaFomento.objects.all(),
        write_only=True,
        source="agencias_fomento",
        many=True,
    )

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
            "pesquisador_projeto",
            "agencias_fomento",
            "agencias_fomento_ids",
        ]

    def create(self, validated_data):
        area = validated_data.pop("area")
        subareas = validated_data.pop("subarea")
        producoes_academicas = validated_data.pop("producoes_academicas", [])
        valores_arrecadados = validated_data.pop("valores_arrecadados", [])
        agencias_fomento = validated_data.pop("agencias_fomento", [])
        pesquisadores_projeto_data = validated_data.pop("pesquisador_projeto")
        projeto = Projeto.objects.create(area=area, **validated_data)
        projeto.subarea.set(subareas)
        projeto.agencias_fomento.set(agencias_fomento)

        for producao_academica in producoes_academicas:
            ProducaoAcademica.objects.create(projeto=projeto, **producao_academica)

        for valor_arrecadado in valores_arrecadados:
            ValorArrecadado.objects.create(projeto=projeto, **valor_arrecadado)

        for pesquisador in pesquisadores_projeto_data:
            PesquisadorProjeto.objects.create(projeto=projeto, **pesquisador)
        return projeto

    def get_pesquisadores(self, obj):
        """Get pesquisadores"""
        pesquisadores = []
        for pesquisador_projeto in obj.pesquisadores.all():
            pesquisadores.append(
                PesquisadorListInProjectDetail(pesquisador_projeto).data
            )
        return pesquisadores

    def validate_pesquisador_projeto(self, value):
        """Pesquisador projeto validate"""
        coord_count = 0
        for pesquisador_projeto in value:
            if pesquisador_projeto["cargo"] == "COORDENADOR":
                coord_count += 1
        if coord_count != 1:
            raise serializers.ValidationError("O projeto deve ter um coordenador")
        return value


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
