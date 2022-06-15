from rest_framework import serializers
from disease_recommendations.models import Disease, Recommendation, DiseaseTag
from products.models import Product


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


class ProductRecommendationSerializer(serializers.ModelSerializer):\

    class RecommendationSerializer(serializers.ModelSerializer):
        disease = serializers.CharField(source='disease.name')
        code = serializers.SerializerMethodField()

        class Meta:
            model = Recommendation
            fields = ('percent', 'description', 'disease', 'code')

        def get_code(self, obj: Recommendation):
            return Recommendation.get_verdict(obj)['code']

    recommendations = serializers.SerializerMethodField()
    verdict = serializers.SerializerMethodField()
    category = serializers.CharField(source='category.name')

    def get_recommendations(self, obj: Product):
        return self.RecommendationSerializer(instance=obj.pref_recommendations, many=True).data

    def get_verdict(self, obj: Product):
        recommendation = obj.pref_recommendations[0] if obj.pref_recommendations else None
        return Recommendation.get_verdict(recommendation)

    class Meta:
        model = Product
        fields = ('uuid', 'name', 'category', 'price', 'description', 'photo_link', 'recommendations', 'verdict')