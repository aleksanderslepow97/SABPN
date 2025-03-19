# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User, Invite
from .serializers import UserSerializer, InviteSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """Представление для работы с пользователями."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class InviteViewSet(viewsets.ModelViewSet):
    """Представление для работы с инвайтами."""
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Создание пользователя по номеру телефона."""
        code = self.generate_invite_code()
        serializer.save(code=code)

    def generate_invite_code(self):
        """Генерирует уникальный инвайт-код."""
        import random
        import string
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
