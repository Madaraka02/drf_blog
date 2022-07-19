from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class RegisterUserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username', 'email']