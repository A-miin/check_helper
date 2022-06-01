from django.contrib.auth import get_user_model
from django.db.transaction import atomic
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from accounts.serializers import (
    UserSerializer,
    AddDeleteDiseaseUserSerializer,
    RecommendationSerializer, RecsSerializer,
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

    def get(self, request, *args, **kwargs):
        diseases = request.user.diseases.all().values_list('id', flat=True)
        return Response(diseases, status=200)

    @atomic
    def patch(self, request, *args, **kwargs):
        serializer = AddDeleteDiseaseUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.diseases.clear()
        request.user.diseases.add(*serializer.validated_data['ids'])
        return Response({'detail': _('Болезни изменены')}, status=200)

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


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 25


class UserRecommendationsListAPIView(APIView):
    # serializer_class = RecsSerializer
    permission_classes = [permissions.IsAuthenticated]

    # pagination_class = StandardResultsSetPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['product', 'disease']
    def get(self, request, *args, **kwargs):
        serializer = RecsSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        # print('seriaizer=', serializer.data)
        return Response(serializer.data)
