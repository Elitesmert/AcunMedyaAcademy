from rest_framework import serializers
from .models import VideoModel


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoModel
        fields = '__all__'
