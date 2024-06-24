"""area and subarea serializers module"""

from rest_framework import serializers
from projac.models import Area, SubArea

class AreaSerializer(serializers.ModelSerializer):
    """Area serializer"""

    class Meta:
        """Meta class"""

        model = Area
        fields = ["id", "nome", "cor"]


class SubAreaSerializer(serializers.ModelSerializer):
    """SubArea serializer"""

    cor = serializers.CharField(source="area.cor")

    class Meta:
        """Meta class"""

        model = SubArea
        fields = ["id", "nome","cor"]
