"""views module"""

from rest_framework import viewsets
from projac.models import Pesquisador, Projeto
from .serializers import (
    PesquisadorListSerializer,
    PesquisadorDetailSerializer,
    ProjetoDetailSerializer,
    ProjetoListSerializer,
)


class ProjetoViewSet(viewsets.ModelViewSet):
    """Projeto viewset"""

    queryset = Projeto.objects.all()

    def get_serializer_class(self):
        """Get serializer class method"""
        if self.action == "list":
            return ProjetoListSerializer
        return ProjetoDetailSerializer


class PesquisadorViewSet(viewsets.ModelViewSet):
    """Pesquisador viewset"""

    queryset = Pesquisador.objects.all()

    def get_serializer_class(self):
        """Get serializer class method"""
        if self.action == "list":
            return PesquisadorListSerializer
        return PesquisadorDetailSerializer
