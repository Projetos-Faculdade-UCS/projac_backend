"""projeto serializers module"""

from rest_framework import serializers
from projac.models import Area, PesquisadorProjeto, Projeto, SubArea
from .pesquisador import PesquisadorProjectListSerializer, PesquisadorListInProjectDetail
from .producao_academica import ProducaoAcademicaSerializer
from .valor_arrecadado import ValorArrecadadoSerializer
from .agencia_fomento import AgenciaFomentoSerializer
from .area_subarea import AreaSerializer, SubAreaSerializer


class ProjetoDetailSerializer(serializers.ModelSerializer):
    """Projeto detail serializer"""

    status = serializers.SerializerMethodField()
    area = AreaSerializer(read_only=True)
    area_id = serializers.PrimaryKeyRelatedField(
        queryset=Area.objects.all(), write_only=True, source="area"
    )
    subarea = SubAreaSerializer(read_only=True, many=True)
    subarea_ids = serializers.PrimaryKeyRelatedField(
        queryset=SubArea.objects.all(), write_only=True, source="subarea", many=True
    )
    producoes_academicas = ProducaoAcademicaSerializer(many=True, required=False)
    valor_total_arrecadado = serializers.SerializerMethodField()
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
        projeto = Projeto.objects.create(area=area, **validated_data)
        projeto.subarea.set(subareas)
        return projeto

    def get_status(self, obj):
        """Get status"""
        if obj.cancelado:
            return "CANCELADO"
        elif obj.data_conclusao:
            return "CONCLUIDO"
        return "EM_ANDAMENTO"

    def get_valor_total_arrecadado(self, obj):
        """Get valor total arrecadado"""
        total = 0
        for valor in obj.valores_arrecadados.all():
            total += valor.valor
        return total

    def get_pesquisadores(self, obj):
        """Get pesquisadores"""
        pesquisadores = []
        for pesquisador_projeto in obj.pesquisadorprojeto_set.all():
            pesquisadores.append(PesquisadorListInProjectDetail(pesquisador_projeto).data)
        return pesquisadores

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
