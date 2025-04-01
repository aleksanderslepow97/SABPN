# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя для системы авторизации по номеру телефона.

    Атрибуты:
        phone_number (CharField): Номер телефона пользователя, должен быть уникальным.
        invite_code (CharField): Код приглашения, связанный с пользователем.
    """
    # objects = None
    phone_number = models.CharField(max_length=15, unique=True, verbose_name="Номер телефона")
    invite_code = models.CharField(max_length=10, unique=True, verbose_name="Инвайт-код")

    def __str__(self):
        """Возвращает строковое представление пользователя, отображающее номер телефона."""
        return self.phone_number


class Invite(models.Model):
    """Модель инвайта для управления кодами приглашений.

    Атрибуты:
        code (CharField): Уникальный код приглашения, который используется для предоставления доступа.
    """
    objects = None
    code = models.CharField(max_length=10, unique=True, verbose_name="Инвайт-код")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    def __str__(self):
        """Возвращает строковое представление инвайта, отображающее код."""
        return self.code
