from rest_framework import routers
from django.urls import path, include
from projac.views import TesteAuthApiView

router = routers.DefaultRouter()



urlpatterns = [
    path('', include(router.urls)),
    path('teste-auth/', TesteAuthApiView.as_view(), name='teste-auth'),
]