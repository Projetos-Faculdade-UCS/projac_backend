from rest_framework import serializers

from projac.models import Pesquisador, PesquisadorProjeto


class GraphSerializer(serializers.ModelSerializer):
    # Custom field to get the Projeto IDs
    projetos = serializers.SerializerMethodField()

    class Meta:
        model = Pesquisador
        fields = [
            "id",
            "nome",
            "sobrenome",
            "foto_perfil",
            "projetos",
        ]

    def get_projetos(self, obj):
        # Get all related PesquisadorProjeto objects for the current Pesquisador
        pesquisador_projetos = PesquisadorProjeto.objects.filter(pesquisador=obj)
        # Return a list of Projeto IDs
        return [
            pesquisador_projeto.projeto.pk
            for pesquisador_projeto in pesquisador_projetos
        ]
