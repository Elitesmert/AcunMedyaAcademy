from rest_framework import serializers
from .models import CustomUserModel


class UserSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField(method_name='get_user_group')
    lesson = serializers.SerializerMethodField(method_name='get_user_lessons')

    class Meta:
        model = CustomUserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'slug', 'avatar', 'group', 'lesson', 'period',
                  'birth_date', 'github_link', 'linkedin_link', 'instagram_link']

    def get_user_group(self, obj):
        return str(obj.groups.name)

    def get_user_lessons(self, obj):
        lesson = obj.department.first()
        return str(lesson.name)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['first_name', 'last_name', 'avatar', 'birth_date', 'github_link', 'linkedin_link', 'instagram_link']
