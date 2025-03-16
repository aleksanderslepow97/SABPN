# Create your tests here.
from django.test import TestCase
from .models import User, Invite
from rest_framework.test import APIClient
from rest_framework import status


class UserModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'phone_number': '1234567890'}

    def test_user_creation(self):
        """Проверка успешного создания пользователя."""
        response = self.client.post('/api/users/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_duplicate_user_creation(self):
        """Проверка обработки дубликатов."""
        self.client.post('/api/users/', self.user_data)
        response = self.client.post('/api/users/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class InviteModelTest(TestCase):
    def setUp(self):
        self.invite_data = {'code': 'INVITE123'}
        self.invite = Invite.objects.create(**self.invite_data)

    def test_invite_creation(self):
        """Проверка успешного создания инвайта."""
        invite = Invite.objects.create(code='INVITE456')
        self.assertEqual(invite.code, 'INVITE456')

    def test_list_users_by_invite_code(self):
        """Проверка успешного получения пользователей по инвайт-коду."""
        user = User.objects.create(phone_number='1234567890', invite_code='INVITE123')
        response = self.client.get('/api/invites/INVITE123/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
