from rest_framework import serializers
from disease_recommendations.models import Disease, Recommendation, DiseaseTag


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'


class DiseaseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseTag
        fields = '__all__'


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'


class SimpleDiseaseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseTag
        fields = ('id', 'name',)
