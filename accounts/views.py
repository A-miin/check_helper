from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from rest_framework.views import APIView
from rest_framework import permissions

from accounts.serializers import (
    UserSerializer,
    AddDeleteDiseaseUserSerializer,
    RecommendationSerializer,
)
from rest_framework import status, permissions
from rest_framework.response import Response

from disease_recommendations.models import Disease, Recommendation


class ListCreateUsersAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': _('You do not have permission to perform this action.')},
                            status=status.HTTP_403_FORBIDDEN)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroyUsersAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = super(RetrieveUpdateDestroyUsersAPIView, self).get_object()
        if self.request.user.is_staff:
            return user
        else:
            return self.request.user


@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_id=_('Add diseases to user endpoint'),
    tags=['user'],
    request_body=AddDeleteDiseaseUserSerializer,
    responses={
        status.HTTP_200_OK: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'detail': openapi.Schema(type=openapi.TYPE_STRING, default='Болезни добавлены'),
            }
        ),
    }
))
@method_decorator(name='delete', decorator=swagger_auto_schema(
    operation_id=_('Remove diseases from user endpoint'),
    tags=['user'],
    request_body=AddDeleteDiseaseUserSerializer,
    responses={
        status.HTTP_204_NO_CONTENT: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'detail': openapi.Schema(type=openapi.TYPE_STRING, default='Болезни добавлены'),
            }
        ),
    }
))
class AddDeleteDiseaseAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = AddDeleteDiseaseUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user.diseases.add(*serializer.validated_data['ids'])
        return Response({'detail': _('Болезни добавлены')}, status=200)

    def delete(self, request, *args, **kwargs):
        serializer = AddDeleteDiseaseUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user.diseases.remove(*serializer.validated_data['ids'])
        return Response({'detail': _('Болезни удалены')}, status=204)


class UserRecommendationsListAPIView(ListAPIView):
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user_diseases = Disease.objects.filter(users=self.request.user)
        queryset = Recommendation.objects.filter(disease__in=current_user_diseases)
        return queryset
