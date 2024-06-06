"""producao academica serializer module"""

from rest_framework import serializers
from projac.models import ProducaoAcademica

class ProducaoAcademicaSerializer(serializers.ModelSerializer):
    """ProducaoAcademica serializer"""

    class Meta:
        """Meta class"""

        model = ProducaoAcademica
        exclude = ["id", "projeto"]
