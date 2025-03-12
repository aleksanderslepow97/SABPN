# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .models import User, InviteCode
from .serializers import UserSerializer, InviteCodeSerializer

class UserViewSet(viewsets.ModelViewSet):
    """Представления для работы с пользователями."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class InviteCodeViewSet(viewsets.ModelViewSet):
    """Представления для работы с инвайт-кодами."""

    queryset = InviteCode.objects.all()
    serializer_class = InviteCodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Создает инвайт-код для пользователя."""
        user_id = request.data.get('user')
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        invite_code = InviteCode.objects.create(code=code, user_id=user_id)
        serializer = self.get_serializer(invite_code)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
