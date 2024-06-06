"""init module for serializers."""

from projac.serializers.area_subarea import AreaSerializer, SubAreaSerializer
from projac.serializers.pesquisador import (
    PesquisadorDetailSerializer,
    PesquisadorProjectListSerializer,
    PesquisadorProjetoSerializer,
)
from projac.serializers.producao_academica import ProducaoAcademicaSerializer
from projac.serializers.valor_arrecadado import ValorArrecadadoSerializer
from projac.serializers.agencia_fomento import AgenciaFomentoSerializer
from projac.serializers.projeto import ProjetoDetailSerializer, ProjetoListSerializer


__all__ = [
    "PesquisadorDetailSerializer",
    "PesquisadorProjetoSerializer",
    "PesquisadorProjectListSerializer",
    "ProducaoAcademicaSerializer",
    "ValorArrecadadoSerializer",
    "AgenciaFomentoSerializer",
    "AreaSerializer",
    "SubAreaSerializer",
    "ProjetoDetailSerializer",
    "ProjetoListSerializer",
]
