from django.urls import path
from disease_recommendations.views import DiseaseListAPIView

urlpatterns = [
    path('diseases/', DiseaseListAPIView.as_view(), name='disease-list'),
]
