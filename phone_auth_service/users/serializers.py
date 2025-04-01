from rest_framework import serializers
from .models import User, Invite


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя.

    Используется для валидации и сериализации данных, связанных с пользователем.

    Атрибуты:
        phone_number (str): Номер телефона пользователя.
        invite_code (str): Код приглашения пользователя (необязательный).
    """
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'invite_code']


class InviteSerializer(serializers.ModelSerializer):
    """Сериализатор для модели инвайта.

    Используется для обработки данных, связанных с кодами приглашений.

    Атрибуты:
        code (str): Код приглашения.
    """
    class Meta:
        model = Invite
        fields = ['id', 'code', 'is_active']
