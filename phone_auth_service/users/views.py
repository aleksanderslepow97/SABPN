#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Invite
from .serializers import UserSerializer, InviteSerializer
import random
import string


def generate_invite_code(length=10):
    """Генерирует уникальный инвайт-код."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


class UserViewSet(viewsets.ModelViewSet):
    """Представление для работы с пользователями."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        """Создание пользователя по номеру телефона."""
        phone_number = request.data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            return Response({"error": "Пользователь уже существует."}, status=status.HTTP_400_BAD_REQUEST)

        invite_code = generate_invite_code()
        user = User.objects.create(phone_number=phone_number, invite_code=invite_code)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


def list_users(request, code):
    """Получение пользователей по инвайт-коду."""
    users = User.objects.filter(invite_code=code)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class InviteViewSet(viewsets.ModelViewSet):
    """Представление для работы с инвайтами."""
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

    def create(self, request):
        """Создание инвайт-кода."""
        invite_code = generate_invite_code()
        invite = Invite.objects.create(code=invite_code)
        return Response(InviteSerializer(invite).data, status=status.HTTP_201_CREATED)
