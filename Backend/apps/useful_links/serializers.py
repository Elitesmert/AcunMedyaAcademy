from rest_framework import serializers
from .models import UsefulLinksModel


class UsefulLinksSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(method_name='get_username')
    user_avatar = serializers.SerializerMethodField(method_name='get_user_avatar')

    class Meta:
        model = UsefulLinksModel
        fields = ['name', 'link', 'username', 'user_avatar', 'language', 'created_on', 'updated_on']

    def get_username(self, obj):
        return str(obj.author.username)

    def get_user_avatar(self, obj):
        return str(obj.author.avatar.url)
