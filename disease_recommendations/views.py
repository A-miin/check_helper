from rest_framework.generics import ListAPIView
from disease_recommendations.models import Disease
from disease_recommendations.serializers import DiseaseSerializer
from rest_framework import permissions


class DiseaseListAPIView(ListAPIView):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all()
    permission_classes = [permissions.IsAuthenticated]
