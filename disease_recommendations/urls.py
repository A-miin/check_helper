from django.urls import path
from disease_recommendations.views import (
    DiseaseListAPIView,
    DiseaseTagListAPIView,
    RecommendationListAPIView
)

urlpatterns = [
    path('diseases/', DiseaseListAPIView.as_view(), name='disease-list'),
    path('diseasetags/', DiseaseTagListAPIView.as_view(), name='diseasetag-list'),
    path('recommendations/', RecommendationListAPIView.as_view(), name='recs-list'),
]

