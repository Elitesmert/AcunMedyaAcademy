from rest_framework import serializers
from .models import VideoModel, VideoCommentModel


class VideosSerializer(serializers.ModelSerializer):
    instructor_slug = serializers.SerializerMethodField(method_name='get_instructor_slug')

    class Meta:
        model = VideoModel
        fields = ['title', 'slug', 'description', 'video_file', 'created_on', 'updated_on', 'instructor',
                  'instructor_slug']

    def get_instructor_slug(self, obj):
        return str(obj.instructor.slug)


class VideoCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

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
