from rest_framework.views import APIView 
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.response import Response

# Create your views here.

class TesteAuthApiView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request):
        return Response({'message': 'hello world!'})
