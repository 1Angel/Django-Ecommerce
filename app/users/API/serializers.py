from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import Account
from django.contrib import auth


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields ="__all__"

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance







class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'El passwor de confirmacion no coincide'})

        if Account.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'El email del usuario ya existe'})

        account =Account.objects.create_user(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            password=self.validated_data['password'],
        )
        account.set_password = self.validated_data['password']

        account.save()
        return account