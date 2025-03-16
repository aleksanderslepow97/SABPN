from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, InviteViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'invites', InviteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('invites/<str:code>/users/', InviteViewSet.as_view({'get': 'list_users'}), name='list_users_by_invite'),
]
