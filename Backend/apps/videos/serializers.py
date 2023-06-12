from rest_framework import serializers
from .models import VideoModel


class VideosSerializer(serializers.ModelSerializer):
    instructor_slug = serializers.SerializerMethodField(method_name='get_instructor_slug')

    class Meta:
        model = VideoModel
        fields = ['title', 'slug', 'description', 'video_file', 'created_on', 'updated_on', 'instructor',
                  'instructor_slug']

    def get_instructor_slug(self, obj):
        return str(obj.instructor.slug)
