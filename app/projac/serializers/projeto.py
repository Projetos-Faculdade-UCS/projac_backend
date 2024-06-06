"""projeto serializers module"""

from rest_framework import serializers
from projac.models import Area, PesquisadorProjeto, Projeto, SubArea
from .pesquisador import PesquisadorProjectListSerializer, PesquisadorProjetoSerializer
from .producao_academica import ProducaoAcademicaSerializer
from .valor_arrecadado import ValorArrecadadoSerializer
from .agencia_fomento import AgenciaFomentoSerializer
from .area_subarea import AreaSerializer, SubAreaSerializer


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
    pesquisadores = PesquisadorProjetoSerializer(many=True, required=False)
    producoes_academicas = ProducaoAcademicaSerializer(many=True, required=False)
    valores_arrecadados = ValorArrecadadoSerializer(many=True, required=False)
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
            "valor_solicitado",
            "cancelado",
            "area",
            "area_id",
            "subarea",
            "subarea_ids",
            "pesquisadores",
            "producoes_academicas",
            "valores_arrecadados",
            "agencias_fomento",
        ]

    def create(self, validated_data):
        area = validated_data.pop("area")
        subareas = validated_data.pop("subarea")
        projeto = Projeto.objects.create(area=area, **validated_data)
        projeto.subarea.set(subareas)
        return projeto


class ProjetoListSerializer(serializers.ModelSerializer):
    """Projeto list serializer"""

    area = AreaSerializer(read_only=True)
    status = serializers.SerializerMethodField()
    coordenador = serializers.SerializerMethodField()

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

    def get_status(self, obj):
        """Get status"""
        if obj.cancelado:
            return "CANCELADO"
        elif obj.data_conclusao:
            return "CONCLUIDO"
        return "EM_ANDAMENTO"

    def get_coordenador(self, obj):
        """Get coordenador"""
        try:
            coord = obj.pesquisadorprojeto_set.get(cargo="Coordenador")
            return PesquisadorProjectListSerializer(coord.pesquisador).data
        except PesquisadorProjeto.DoesNotExist:
            return None
