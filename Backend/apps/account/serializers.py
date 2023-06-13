from rest_framework import serializers
from .models import CustomUserModel, DepartmentModel, RolesModel


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesModel
        exclude = ['id', 'permissions']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        exclude = ['id']


class UserSerializer(serializers.ModelSerializer):
    groups = RoleSerializer()
    department = DepartmentSerializer(many=True)

    class Meta:
        model = CustomUserModel
        exclude = ['password', 'user_permissions']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['first_name', 'last_name', 'avatar', 'birth_date', 'github_link', 'linkedin_link', 'instagram_link']
