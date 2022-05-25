from collections import OrderedDict

from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import User
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators
from disease_recommendations.models import Disease, Recommendation
from phonenumber_field.serializerfields import PhoneNumberField

from products.models import Product


class UserDiseasesSerializer(serializers.ModelSerializer):
    def get_queryset(self):
        user = self.context['request'].user
        queryset = user.diseases.all()
        return queryset

    class Meta:
        model = Disease
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    diseases = UserDiseasesSerializer(many=True, read_only=True)
    phone_number = PhoneNumberField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'firstname',
            'lastname',
            'email',
            'phone_number',
            'avatar',
            'password',
            'diseases',
        )

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get('password')
        if password:
            validators.validate_password(password=password, user=user)
            attrs['password'] = make_password(password)
        return super(UserSerializer, self).validate(attrs)


class AddDeleteDiseaseUserSerializer(serializers.Serializer):
    ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Disease.objects.all())


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
        )


class UserProductRecommendationSerializer(serializers.Serializer):
    recommendations = RecommendationSerializer(many=True)
    product = ProductSerializer()


class RecsSerializer(serializers.Serializer):
    data = UserProductRecommendationSerializer(many=True, read_only=True)

    def validate(self, attrs):
        attrs = []
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        user_recs = Recommendation.objects.filter(disease__users=user)
        products = Product.objects.filter(recommendations__in=user_recs)
        for product in products:
            data = {"product": product, 'recommendations': user_recs.filter(product=product)}
            attrs.append(data)
        print('attrs = ', attrs)
        return {"data": attrs}
