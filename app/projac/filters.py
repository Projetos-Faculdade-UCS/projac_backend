"""filters module"""

from django.db.models import Q
from django_filters import CharFilter
from django_property_filter import PropertyCharFilter, PropertyFilterSet
from projac.models import Projeto


class ProjetoFilter(PropertyFilterSet):
    """Projeto filter class"""

    q = CharFilter(field_name="q", method="search_q")
    area = PropertyCharFilter(field_name="area__nome", lookup_expr="exact")
    status = PropertyCharFilter(field_name="status", lookup_expr="exact")

    class Meta:
        """Meta class"""

        model = Projeto
        fields = [
            "area",
            "status",
        ]

    def search_q(self, queryset, _name, value):
        """search_query method"""
        return queryset.filter(
            Q(titulo__icontains=value)
            | self._filter_full_name_coord(value)
        ).distinct()

    def _filter_full_name_coord(self, value):
        return Q(pesquisadores__cargo="Coordenador") & \
            Q(pesquisadores__pesquisador__full_name__icontains=value)
