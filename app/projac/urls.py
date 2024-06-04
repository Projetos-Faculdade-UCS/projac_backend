"""urls module"""

from rest_framework import routers
from django.urls import path, include
from projac.views import ProjetoViewSet

router = routers.DefaultRouter()
router.register("projetos", ProjetoViewSet, basename="projetos")


urlpatterns = [
    path('', include(router.urls)),
]
