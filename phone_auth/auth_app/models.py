from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    """Модель пользователя."""
    phone_number = models.CharField(max_length=15, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

class InviteCode(models.Model):
    """Инвайт код."""
    code = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
