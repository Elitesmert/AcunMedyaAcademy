from rest_framework import serializers
from .models import CoursesModel
from ..account.models import CustomUserModel


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['id', 'username']


class CoursesSerializer(serializers.ModelSerializer):
    instructors = serializers.SerializerMethodField('get_course_instructors')

    class Meta:
        model = CoursesModel
        exclude = ['id']

    def get_course_instructors(self, obj):
        instructors = obj.users.filter(groups=2)
        serializer = InstructorSerializer(instructors, many=True)
        return serializer.data
