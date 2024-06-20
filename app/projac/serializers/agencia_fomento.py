"""agencia fomento serializer module."""

from rest_framework import serializers
from projac.models import AgenciaFomento

class AgenciaFomentoSerializer(serializers.ModelSerializer):
    """AgenciaFomento serializer"""

    class Meta:
        """Meta class"""

        model = AgenciaFomento
        exclude = ["id"]
