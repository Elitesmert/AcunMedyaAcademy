from rest_framework import serializers
from .models import UsefulLinksModel
from ..account.serializers import UserSerializer


class UsefulLinksSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = UsefulLinksModel
        fields = '__all__'
