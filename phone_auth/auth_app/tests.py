# from django.test import TestCase

# Create your tests here.

from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, InviteCode

class UserTests(APITestCase):
    def test_create_user(self):
        """Тест создания пользователя."""
        response = self.client.post('/api/users/', {'phone_number': '1234567890'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invite_code(self):
        """Тест создания инвайт-кода."""
        self.client.post('/api/users/', {'phone_number': '1234567890'})
        user = User.objects.first()
        response = self.client.post('/api/invitecodes/', {'user': user.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
