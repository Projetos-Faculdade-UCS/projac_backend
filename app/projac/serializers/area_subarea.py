"""area and subarea serializers module"""

from rest_framework import serializers
from projac.models import Area, SubArea

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
