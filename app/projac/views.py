from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey

# Create your views here.

class TesteAuthApiView(APIView):
    permission_classes = [HasAPIKey | IsAuthenticated]

    def get(self, request):
        return Response({'message': 'hello world!'})
