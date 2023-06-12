from django.contrib import admin
from .models import VideoModel, VideoCommentModel

admin.site.register(VideoModel)
admin.site.register(VideoCommentModel)