from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from disease_recommendations.models import (
    Disease,
    DiseaseTag,
    Recommendation,
)
from disease_recommendations.serializers import (
    DiseaseSerializer,
    DiseaseTagSerializer,
    RecommendationSerializer,
)
from rest_framework import permissions, filters


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 25


class DiseaseListAPIView(ListAPIView):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all()
    search_fields = ['name']
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]


class DiseaseTagListAPIView(ListAPIView):
    serializer_class = DiseaseTagSerializer
    queryset = DiseaseTag.objects.all()
    search_fields = ['name']
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]


class RecommendationListAPIView(ListAPIView):
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all()
    search_fields = ['product__name', 'disease__name']
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]
