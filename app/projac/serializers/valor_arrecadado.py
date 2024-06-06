"""valor arrecadado serializer module."""

from rest_framework import serializers
from projac.models import ValorArrecadado

class ValorArrecadadoSerializer(serializers.ModelSerializer):
    """ValorArrecadado serializer"""

    class Meta:
        """Meta class"""

        model = ValorArrecadado
        exclude = ["id", "projeto"]
