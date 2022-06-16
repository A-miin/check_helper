from django.db.models import Prefetch
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination

from disease_recommendations.filterset import DiseaseTagFilterSet, DiseaseFilterSet
from disease_recommendations.models import (
    Disease,
    DiseaseTag,
    Recommendation,
)
from disease_recommendations.serializers import (
    DiseaseSerializer,
    DiseaseTagSerializer,
    RecommendationSerializer, SimpleDiseaseTagSerializer, ProductRecommendationSerializer,
)
from rest_framework import permissions, filters

from products.models import Product


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 30


class DiseaseListAPIView(ListAPIView):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all().distinct()
    filterset_class = DiseaseFilterSet
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]


class DiseaseTagListAPIView(ListAPIView):
    serializer_class = DiseaseTagSerializer
    queryset = DiseaseTag.objects.all()
    permission_classes = [permissions.AllowAny]


class RecommendationListAPIView(ListAPIView):
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all()
    search_fields = ['product__name', 'disease__name']
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.AllowAny]
    filterset_class = DiseaseFilterSet


class BarcodeRecommendationView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductRecommendationSerializer

    def get(self, request, *args, **kwargs):
        self.disease_ids = request.GET.get('disease_ids')
        if self.disease_ids:
            self.disease_ids = [int(i) for i in self.disease_ids.split(',')]
        return super(BarcodeRecommendationView, self).get(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super(BarcodeRecommendationView, self).get_serializer_context()
        context['disease_ids'] = self.disease_ids
        return context

    def get_queryset(self):
        qs = Product.objects.all()
        prefetched = Recommendation.objects.all().order_by('-percent')
        if self.disease_ids:
            prefetched = prefetched.filter(disease__in=self.disease_ids)
        qs = qs.prefetch_related(Prefetch('recommendations', queryset=prefetched, to_attr='pref_recommendations'))
        return qs

    def get_object(self):
        return get_object_or_404(self.get_queryset(), uuid=self.kwargs.get('code'))


