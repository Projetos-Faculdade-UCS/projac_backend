"""views module"""

from rest_framework import viewsets
from rest_framework_api_key.permissions import HasAPIKey

from projac.filters import (
    AgenciaFomentoFilter,
    AreaFilter,
    PesquisadorFilter,
    ProducaoAcademicaFilter,
    ProjetoFilter,
    SubAreaFilter,
)
from projac.models import (
    AgenciaFomento,
    Area,
    Pesquisador,
    ProducaoAcademica,
    Projeto,
    SubArea,
)

from .serializers import (
    AgenciaFomentoSerializer,
    AreaSerializer,
    PesquisadorDetailSerializer,
    PesquisadorListSerializer,
    ProducaoAcademicaSerializer,
    ProjetoDetailSerializer,
    ProjetoListSerializer,
    SubAreaSerializer,
    GraphSerializer,
)


class ProjetoViewSet(viewsets.ModelViewSet):
    """Projeto viewset"""

    queryset = Projeto.objects.all()
    filterset_class = ProjetoFilter
    permission_classes = [HasAPIKey]

    def get_serializer_class(self):
        """Get serializer class method"""
        if self.action == "list":
            return ProjetoListSerializer
        return ProjetoDetailSerializer


class PesquisadorViewSet(viewsets.ModelViewSet):
    """Pesquisador viewset"""

    queryset = Pesquisador.objects.all()
    filterset_class = PesquisadorFilter
    permission_classes = [HasAPIKey]

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
    permission_classes = [HasAPIKey]


class SubAreaViewSet(viewsets.ReadOnlyModelViewSet):
    """SubArea viewset"""

    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer
    filterset_class = SubAreaFilter
    permission_classes = [HasAPIKey]


class AgenciaFomentoViewSet(viewsets.ReadOnlyModelViewSet):
    """AgenciaFomento viewset"""

    queryset = AgenciaFomento.objects.all()
    serializer_class = AgenciaFomentoSerializer
    filterset_class = AgenciaFomentoFilter
    permission_classes = [HasAPIKey]


class ProducaoAcademicaViewSet(viewsets.ReadOnlyModelViewSet):
    """ProducoesAcademicas viewset"""

    queryset = ProducaoAcademica.objects.all()
    serializer_class = ProducaoAcademicaSerializer
    filterset_class = ProducaoAcademicaFilter
    permission_classes = [HasAPIKey]

class GraphViewSet(viewsets.ReadOnlyModelViewSet):
    """Graph viewset"""

    queryset = Pesquisador.objects.all()
    serializer_class = GraphSerializer
    permission_classes = []

    def get_queryset(self):
        """Get queryset method"""
        return Pesquisador.objects.prefetch_related("projetos").all()