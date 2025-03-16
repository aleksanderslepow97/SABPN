# from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    """Модель пользователя."""
    objects = None
    phone_number = models.CharField(max_length=15, unique=True, verbose_name="Номер телефона")
    invite_code = models.CharField(max_length=10, unique=True, verbose_name="Инвайт-код")

    def __str__(self):
        return self.phone_number


class Invite(models.Model):
    """Модель инвайт-кода."""
    objects = None
    code = models.CharField(max_length=10, unique=True, verbose_name="Инвайт-код")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    def __str__(self):
        return self.code
