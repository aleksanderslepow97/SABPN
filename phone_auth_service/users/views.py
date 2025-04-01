# Create your views here.
from requests import Response
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action

from .models import User, Invite
from .serializers import UserSerializer, InviteSerializer
# from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


class UserViewSet(viewsets.ModelViewSet):
    """Представление для работы с пользователями."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone')
        if phone_number and User.objects.filter(phone=phone_number).exists():
            return Response(
                {"error": "User with this phone already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)


def generate_invite_code():
    """Генерирует уникальный инвайт-код."""
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


class InviteViewSet(viewsets.ModelViewSet):
    """Представление для работы с инвайтами."""

    @action(detail=True, methods=['get'], url_path='users')
    def list_users(self, request, pk=None):
        invite = self.get_object()
        users = User.objects.filter(invited_by=invite.code)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        """Создание пользователя по номеру телефона."""
        code = generate_invite_code()
        serializer.save(code=code)


def index(request):
    return render(request, 'frontend/index.html')


class PhoneAuthView(View):
    """
    PhoneAuthView - Представление для авторизации пользователей по номеру телефона.

    Обрабатывает POST-запросы с номером телефона.
    При успешном выполнении отправляет код на указанный номер телефона.
    """

    @staticmethod
    def post(request):
        """
        Обрабатывает POST-запрос на авторизацию по телефону.

        Параметры:
        request (HttpRequest): Объект запроса, содержащий номер телефона в теле запроса.

        Возвращает:
        JsonResponse: Ответ с сообщением о статусе отправки кода.
        """

        phone_number = request.POST.get('phone')
        if phone_number:
            # Логика отправки кода на номер телефона
            return JsonResponse({'message': f'Код отправлен на номер: {phone_number}'})
        else:
            return JsonResponse({'error': 'Номер телефона не указан'}, status=400)
