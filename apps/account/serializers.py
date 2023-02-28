from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import UniqueValidator

from apps.account.models import CustomUser


class RegisterCustomUserSerializers(serializers.ModelSerializer):
    """Регистрация пользователя"""
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password], min_length=8, max_length=128)
    password2 = serializers.CharField(min_length=8, max_length=128, required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'user_type', 'password', 'password2')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, data):
        pass1 = data.get("password")
        pass2 = data.pop("password2")
        if pass1 != pass2:
            raise serializers.ValidationError({'password': "Passwords fields didn't match."})
        return data

    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email already exists")
        return email

    def create(self, validated_data):
        if validated_data['user_type'] == 'admin':
            user = CustomUser.objects.create_superuser(**validated_data)
        if validated_data['user_type'] == 'user':
            user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginUserSerializer(serializers.ModelSerializer):
    """Авторизация пользователя"""

    email = serializers.EmailField(max_length=150, required=True)
    password = serializers.CharField(max_length=160, min_length=8, write_only=True)

    tokens = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'tokens')

    def get_tokens(self, instance):
        user = CustomUser.objects.get(email=instance['email'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account is not active, please contact your administrator')

        return {
            'email': user.email,
            'tokens': user.tokens
        }
