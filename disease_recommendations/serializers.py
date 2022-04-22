from rest_framework import serializers
from disease_recommendations.models import Disease


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'
