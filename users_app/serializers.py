from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from users_app.models import UserAccounts


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccounts
        fields = ('username', 'email', 'phone', 'is_staff')


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh_token = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh_token)
        data['access'] = str(refresh_token.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = UserAccounts
        fields = ['id', 'username', 'email', 'phone', 'password', 'is_active']

    def create(self, validated_data):
        try:
            user = UserAccounts.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = UserAccounts.objects.create_user(**validated_data)
        return user
