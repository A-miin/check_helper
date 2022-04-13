from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from accounts.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]