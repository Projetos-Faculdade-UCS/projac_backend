from rest_framework import viewsets
from projac.models import Projeto
from projac.serializers import ProjetoSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    

  