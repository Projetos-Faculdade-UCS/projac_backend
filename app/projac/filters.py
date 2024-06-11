"""filters module"""

from django_property_filter import PropertyFilterSet, PropertyCharFilter
from projac.models import Projeto

class ProjetoFilter(PropertyFilterSet):
    """Projeto filter class"""

    titulo = PropertyCharFilter(field_name="titulo", lookup_expr="icontains")
    area = PropertyCharFilter(field_name="area__nome", lookup_expr="exact")
    status = PropertyCharFilter(field_name="status", lookup_expr="exact")
    coordenador = PropertyCharFilter(field_name="coordenador__full_name", lookup_expr="icontains")

    class Meta:
        """Meta class"""
        model = Projeto
        fields = [
            "titulo",
            "area",
            "status",
            "coordenador",
        ]
