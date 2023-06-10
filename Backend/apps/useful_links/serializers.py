from rest_framework import serializers
from .models import UsefulLinksModel


class ListUsefulLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulLinksModel
        fields = ['name', 'link', 'author', 'language', 'created_on', 'updated_on']
