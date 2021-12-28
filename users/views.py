from rest_framework.views import APIView
from rest_framework.response import Response

from users import serializers, models

class UserApiView(APIView):
    serializer_class = serializers.UserSerializer

    def get(self, request, format=None):
        return Response({'Hello': 'funciona'})