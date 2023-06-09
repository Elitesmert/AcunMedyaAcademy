from rest_framework import serializers
from .models import CustomUserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'slug', 'avatar', 'groups', 'department', 'period',
                  'birth_date', 'github_link', 'linkedin_link', 'instagram_link']
