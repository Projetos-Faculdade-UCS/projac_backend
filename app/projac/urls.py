"""urls module"""

from django.urls import include, path
from rest_framework import routers

from projac.views import (
    AgenciaFomentoViewSet,
    AreaViewSet,
    PesquisadorViewSet,
    ProducaoAcademicaViewSet,
    ProjetoViewSet,
    SubAreaViewSet,
    GraphViewSet,
)

router = routers.DefaultRouter()
router.register("projetos", ProjetoViewSet, basename="projetos")
router.register("pesquisadores", PesquisadorViewSet, basename="pesquisadores")
router.register("areas", AreaViewSet, basename="areas")
router.register("subareas", SubAreaViewSet, basename="subareas")
router.register("agencias-fomento", AgenciaFomentoViewSet, basename="agencias-fomento")
router.register(
    "producoes-academicas", ProducaoAcademicaViewSet, basename="producoes-academicas"
)
router.register("graph", GraphViewSet, basename="graph")


urlpatterns = [
    path("", include(router.urls)),
]
