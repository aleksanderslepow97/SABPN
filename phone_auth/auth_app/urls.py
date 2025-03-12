from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, InviteCodeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'invitecodes', InviteCodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
