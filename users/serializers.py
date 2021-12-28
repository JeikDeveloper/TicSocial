from rest_framework import serializers
from users.models import UserProfile

class UserSerializer(serializers.Serializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email')