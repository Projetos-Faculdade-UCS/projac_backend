"""urls module"""

from rest_framework import routers
from django.urls import path, include
from projac.views import ProjetoViewSet, PesquisadorViewSet

router = routers.DefaultRouter()
router.register("projetos", ProjetoViewSet, basename="projetos")
router.register("pesquisadores", PesquisadorViewSet, basename="pesquisadores")


urlpatterns = [
    path('', include(router.urls)),
]
