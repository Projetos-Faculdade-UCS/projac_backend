"""pesquisador serializers module"""

from projac.models import Pesquisador, PesquisadorProjeto
from rest_framework import serializers


class PesquisadorDetailSerializer(serializers.ModelSerializer):
    """Pesquisador detail serializer"""

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



class PesquisadorProjectListSerializer(serializers.ModelSerializer):
    """Pesquisador project list serializer"""

    class Meta:
        """Meta class"""

        model = Pesquisador
        fields = ['id', 'nome', 'sobrenome']
