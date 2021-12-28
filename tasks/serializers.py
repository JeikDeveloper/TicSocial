from rest_framework import serializers
from tasks.models import TasksOfUser

class Taskserializer(serializers.Serializer):
    class Meta:
        model = TasksOfUser
        fields = ('id', 'username', 'name', 'description')