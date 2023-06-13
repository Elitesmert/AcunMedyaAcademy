from django.urls import path
from .views import ListVideosAPI, UserVideosAPIView, VideoDetailAPI

urlpatterns = [
    path('', ListVideosAPI.as_view(), name='list_videos'),
    path('instructor/<slug>/', UserVideosAPIView.as_view(), name='list_user_videos'),
    path('video/<slug>', VideoDetailAPI.as_view(), name='video_detail')
]