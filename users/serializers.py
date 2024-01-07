from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=10, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'name')

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'], name=validated_data['name'])
        return user

# class UserHabitsSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = UserHabits
#         fields = "__all__"


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         # Добавление пользовательских полей в токен
#         token['username'] = user.username
#         token['email'] = user.email
#
#         return token