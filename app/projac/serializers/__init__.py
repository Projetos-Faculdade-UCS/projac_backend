"""init module for serializers."""

from projac.serializers.agencia_fomento import AgenciaFomentoSerializer
from projac.serializers.area_subarea import AreaSerializer, SubAreaSerializer
from projac.serializers.pesquisador import (
    PesquisadorListInProjectDetail,
    PesquisadorProjectListSerializer,
)
from projac.serializers.producao_academica import ProducaoAcademicaSerializer
from projac.serializers.projeto import ProjetoDetailSerializer, ProjetoListSerializer
from projac.serializers.valor_arrecadado import ValorArrecadadoSerializer

__all__ = [
    "PesquisadorProjectListSerializer",
    "PesquisadorListInProjectDetail",
    "ProducaoAcademicaSerializer",
    "ValorArrecadadoSerializer",
    "AgenciaFomentoSerializer",
    "AreaSerializer",
    "SubAreaSerializer",
    "ProjetoDetailSerializer",
    "ProjetoListSerializer",
]
