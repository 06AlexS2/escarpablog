from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'last_name', 'email', 'username', 'password', 'role', 'is_verified', 'joinedAt')
        extra_kwargs = {'password': {'write_only': True}}