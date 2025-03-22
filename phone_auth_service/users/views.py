# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User, Invite
from .serializers import UserSerializer, InviteSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


class UserViewSet(viewsets.ModelViewSet):
    """Представление для работы с пользователями."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


def generate_invite_code():
    """Генерирует уникальный инвайт-код."""
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


class InviteViewSet(viewsets.ModelViewSet):
    """Представление для работы с инвайтами."""
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    permission_classes = [IsAuthenticated]

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
