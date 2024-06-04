"""serializers module"""

from projac.models import Area, Pesquisador, PesquisadorProjeto, Projeto, SubArea
from rest_framework import serializers


class AreaSerializer(serializers.ModelSerializer):
    """Area serializer"""

    class Meta:
        """Meta class"""

        model = Area
        exclude = ["id"]


class SubAreaSerializer(serializers.ModelSerializer):
    """SubArea serializer"""

    area = AreaSerializer()

    class Meta:
        """Meta class"""

        model = SubArea
        exclude = ["id"]


class PesquisadorSerializer(serializers.ModelSerializer):
    """Pesquisador serializer"""

    class Meta:
        """Meta class"""

        model = Pesquisador
        fields = "__all__"


class PesquisadorProjetoSerializer(serializers.ModelSerializer):
    """PesquisadorProjeto serializer"""

    pesquisador = serializers.SlugRelatedField(
        slug_field="full_name",
        many=False,
        read_only=True,
    )

    class Meta:
        """Meta class"""

        model = PesquisadorProjeto
        fields = "__all__"


class ProjetoSerializer(serializers.ModelSerializer):
    """Projeto serializer"""

    area = AreaSerializer(read_only=True)
    area_id = serializers.PrimaryKeyRelatedField(
        queryset=Area.objects.all(), write_only=True, source="area"
    )
    subarea = SubAreaSerializer(read_only=True, many=True)
    subarea_ids = serializers.PrimaryKeyRelatedField(
        queryset=SubArea.objects.all(), write_only=True, source="subarea", many=True
    )
    pesquisadores = PesquisadorProjetoSerializer(many=True, required=False)

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
        ]

    def create(self, validated_data):
        area = validated_data.pop("area")
        subareas = validated_data.pop("subarea")
        projeto = Projeto.objects.create(area=area, **validated_data)
        projeto.subarea.set(subareas)
        return projeto
