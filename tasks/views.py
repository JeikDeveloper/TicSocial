from rest_framework.views import APIView
from rest_framework.response import Response

from tasks import serializers, models

class TaskAPiView(APIView):
    serializer_class = serializers.Taskserializer

    def get(self, request, format=None):
        return Response({'Hello': 'funciona'})