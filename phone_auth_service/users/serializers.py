from rest_framework import serializers
from .models import User, Invite


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя."""
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'invite_code']


class InviteSerializer(serializers.ModelSerializer):
    """Сериализатор для инвайта."""
    class Meta:
        model = Invite
        fields = ['id', 'code', 'is_active']
