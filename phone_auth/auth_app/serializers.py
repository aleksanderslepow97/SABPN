from rest_framework import serializers
from .models import User, InviteCode

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя."""

    class Meta:
        model = User
        fields = '__all__'

class InviteCodeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели инвайт-кода."""

    class Meta:
        model = InviteCode
        fields = '__all__'
