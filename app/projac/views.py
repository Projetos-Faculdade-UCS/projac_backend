"""views module"""

from projac.filters import (
    AgenciaFomentoFilter,
    AreaFilter,
    ProjetoFilter,
    SubAreaFilter,
)
from projac.models import AgenciaFomento, Area, Pesquisador, Projeto, SubArea
from rest_framework import viewsets

from .serializers import (
    AgenciaFomentoSerializer,
    AreaSerializer,
    PesquisadorDetailSerializer,
    PesquisadorListSerializer,
    ProjetoDetailSerializer,
    ProjetoListSerializer,
    SubAreaSerializer,
)


class ProjetoViewSet(viewsets.ModelViewSet):
    """Projeto viewset"""

    queryset = Projeto.objects.all()
    filterset_class = ProjetoFilter

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


class AreaViewSet(viewsets.ReadOnlyModelViewSet):
    """Area viewset"""

    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    filterset_class = AreaFilter


class SubAreaViewSet(viewsets.ReadOnlyModelViewSet):
    """SubArea viewset"""

    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer
    filterset_class = SubAreaFilter


class AgenciaFomentoViewSet(viewsets.ReadOnlyModelViewSet):
    """AgenciaFomento viewset"""

    queryset = AgenciaFomento.objects.all()
    serializer_class = AgenciaFomentoSerializer
    filterset_class = AgenciaFomentoFilter
