from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import (
    ListCreateUsersAPIView,
    RetrieveUpdateDestroyUsersAPIView,
    AddDeleteDiseaseAPIView,
    UserRecommendationsListAPIView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', ListCreateUsersAPIView.as_view(), name='users-list-create'),
    path('users/<int:pk>/', RetrieveUpdateDestroyUsersAPIView.as_view(), name='users-rud'),
    path('users/<int:pk>/diseases/', AddDeleteDiseaseAPIView.as_view(), name='users-disease'),
    path('users/<int:pk>/recommendations/', UserRecommendationsListAPIView.as_view(), name='users-recommendtaions'),
]
