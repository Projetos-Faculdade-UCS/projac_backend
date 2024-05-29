from rest_framework import serializers
from projac.models import Projeto,Area,SubArea




class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        exclude = ['id']

class SubAreaSerializer(serializers.ModelSerializer):
    area = AreaSerializer()
    class Meta:
        model = SubArea
        exclude = ['id']


class ProjetoSerializer(serializers.ModelSerializer):

    area = AreaSerializer()
    subarea = SubAreaSerializer(many=True)
    class Meta:
        model = Projeto
        fields = '__all__'
        
        
