import datetime

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUserModel, CoursesModel, RolesModel


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesModel
        exclude = ['id', 'permissions']


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesModel
        exclude = ['id']


class UserSerializer(serializers.ModelSerializer):
    groups = RoleSerializer()
    courses = CoursesSerializer(many=True)

    class Meta:
        model = CustomUserModel
        exclude = ['password', 'user_permissions']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['first_name', 'last_name', 'avatar', 'birth_date', 'github_link', 'linkedin_link', 'instagram_link']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['iat'] = datetime.datetime.now()
        token['user'] = user.username
        token['role'] = user.groups.name

        return token
