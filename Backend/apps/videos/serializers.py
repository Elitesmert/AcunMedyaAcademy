from rest_framework import serializers
from .models import VideoModel, VideoCommentModel
from ..account.serializers import UserSerializer


class VideosSerializer(serializers.ModelSerializer):
    instructor = UserSerializer()

    class Meta:
        model = VideoModel
        fields = ['title', 'slug', 'description', 'video_file', 'created_on', 'updated_on', 'instructor']


class VideoCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoModel
        exclude = ['instructor']


class VideoCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    author = UserSerializer()

    class Meta:
        model = VideoCommentModel
        fields = '__all__'

    def validate(self, attrs):
        if attrs['parent']:
            if attrs['parent'].video != attrs['video']:
                raise serializers.ValidationError('Bir hata oluştu')
        return attrs

    def get_replies(self, obj):
        if obj.any_children:
            return VideoCommentSerializer(obj.children(), many=True).data
