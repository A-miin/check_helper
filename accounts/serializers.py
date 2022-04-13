from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import User
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators


class UserSerializer(serializers.ModelSerializer):

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
        )

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get('password')
        validators.validate_password(password=password, user=user)
        attrs['password'] = make_password(password)
        return super(UserSerializer, self).validate(attrs)
