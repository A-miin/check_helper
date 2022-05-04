from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import User
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators
from disease_recommendations.models import Disease
from phonenumber_field.serializerfields import PhoneNumberField


class UserDiseasesSerializer(serializers.ModelSerializer):
    def get_queryset(self):
        user = self.context['request'].user
        queryset = user.diseases.objects.all()
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
        validators.validate_password(password=password, user=user)
        attrs['password'] = make_password(password)
        return super(UserSerializer, self).validate(attrs)


class AddDeleteDiseaseUserSerializer(serializers.Serializer):
    ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Disease.objects.all())