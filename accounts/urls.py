from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import UserViewSet
from rest_framework.routers import DefaultRouter

app_name = "accounts"

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(user_router.urls)),
]
