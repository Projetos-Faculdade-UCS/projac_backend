from rest_framework import serializers

from projac.models import Pesquisador

class GraphSerializer(serializers.ModelSerializer):
    projetos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Pesquisador
        fields = [
            "nome",
            "sobrenome",
            "foto_perfil",
            "projetos",
        ]