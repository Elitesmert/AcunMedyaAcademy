from rest_framework import serializers
from .models import UsefulLinksModel
from ..account.serializers import UserSerializer


class UsefulLinksSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = UsefulLinksModel
        fields = '__all__'


class UsefulLinkCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulLinksModel
        exclude = ['author']
