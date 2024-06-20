"""pesquisador_projeto serializer module"""

from projac.models import Pesquisador, PesquisadorProjeto
from rest_framework import serializers


class PesquisadorProjetoSerializer(serializers.ModelSerializer):
    """PesquisadorProjeto serializer"""

    pesquisador_id = serializers.PrimaryKeyRelatedField(
        queryset=Pesquisador.objects.all(), source="pesquisador", write_only=True
    )

    class Meta:
        model = PesquisadorProjeto
        fields = ["pesquisador_id", "cargo", "horas"]
