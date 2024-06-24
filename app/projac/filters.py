"""filters module"""

from django.db.models import Q
from django_filters import CharFilter, FilterSet
from django_property_filter import PropertyCharFilter, PropertyFilterSet

from projac.models import (
    AgenciaFomento,
    Area,
    Pesquisador,
    ProducaoAcademica,
    Projeto,
    SubArea,
)


class ProjetoFilter(PropertyFilterSet):
    """Projeto filter class"""

    q = CharFilter(field_name="q", method="search_q")
    area = PropertyCharFilter(field_name="area__nome", lookup_expr="exact")
    status = PropertyCharFilter(field_name="status", lookup_expr="exact")

    class Meta:
        """Meta class"""

        model = Projeto
        fields = [
            "q",
            "area",
            "status",
        ]

    def search_q(self, queryset, _name, value):
        """search_query method"""
        return queryset.filter(
            Q(titulo__icontains=value) | self._filter_full_name_coord(value)
        ).distinct()

    def _filter_full_name_coord(self, value):
        return Q(pesquisadores__cargo="Coordenador") & Q(
            pesquisadores__pesquisador__full_name__icontains=value
        )


class PesquisadorFilter(FilterSet):
    """Pesquisador filter class"""

    q = CharFilter(field_name="q", method="search_q")

    class Meta:
        """Meta class"""

        model = Pesquisador
        fields = [
            "q",
        ]

    def search_q(self, queryset, _name, value):
        """search_nome method"""
        return queryset.filter(full_name__icontains=value).distinct()


class AreaFilter(FilterSet):
    """Area filter class"""

    q = CharFilter(field_name="nome", lookup_expr="icontains")

    class Meta:
        """Meta class"""

        model = Area
        fields = [
            "q",
        ]


class SubAreaFilter(FilterSet):
    """SubArea filter class"""

    q = CharFilter(field_name="nome", lookup_expr="icontains")

    class Meta:
        """Meta class"""

        model = SubArea
        fields = [
            "q",
        ]


class AgenciaFomentoFilter(PropertyFilterSet):
    """AgenciaFomento filter class"""

    q = PropertyCharFilter(field_name="full_name", lookup_expr="icontains")

    class Meta:
        """Meta class"""

        model = AgenciaFomento
        fields = [
            "q",
        ]


class ProducaoAcademicaFilter(FilterSet):
    """ProducaoAcademica filter class"""

    q = CharFilter(field_name="titulo", lookup_expr="icontains")

    class Meta:
        """Meta class"""

        model = ProducaoAcademica
        fields = [
            "q",
        ]
