"""urls module"""

from django.urls import include, path
from projac.views import (
    AgenciaFomentoViewSet,
    AreaViewSet,
    PesquisadorViewSet,
    ProjetoViewSet,
    SubAreaViewSet,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("projetos", ProjetoViewSet, basename="projetos")
router.register("pesquisadores", PesquisadorViewSet, basename="pesquisadores")
router.register("areas", AreaViewSet, basename="areas")
router.register("subareas", SubAreaViewSet, basename="subareas")
router.register("agencias", AgenciaFomentoViewSet, basename="agencias")


urlpatterns = [
    path("", include(router.urls)),
]
