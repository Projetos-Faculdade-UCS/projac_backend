"""views module"""

from rest_framework import viewsets
from projac.models import Projeto
from .serializers import ProjetoListSerializer, ProjetoDetailSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    """Projeto viewset"""
    queryset = Projeto.objects.all()

    def get_serializer_class(self):
        """Get serializer class method"""
        if self.action == "list":
            return ProjetoListSerializer
        return ProjetoDetailSerializer
    