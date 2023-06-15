from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user_info')
    user_avatar = serializers.SerializerMethodField('get_user_avatar')
    user_course = serializers.SerializerMethodField('get_user_course')

    class Meta:
        model = Ticket
        fields = '__all__'

    def get_user_info(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    def get_user_avatar(self, obj):
        return obj.user.avatar.url

    def get_user_course(self, obj):
        course = obj.user.courses.first()
        return course.name


class TicketCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ['agent', 'status', 'completed_at', 'user']
