from django.urls import path
from .views import (ListVideosAPI, UserVideosAPIView, VideoDetailAPI, VideoCommentCreateAPI,
                    VideoCommentsListAPI, VideoCreateAPI, VideoUpdateAPI)
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 1)(ListVideosAPI.as_view()), name='list_videos'),
    path('create/', VideoCreateAPI.as_view(), name='create_video'),
    path('update/<slug>/', VideoUpdateAPI.as_view(), name='update_video'),
    path('instructor/<slug>/', UserVideosAPIView.as_view(), name='list_user_videos'),
    path('video/<slug>/', VideoDetailAPI.as_view(), name='video_detail'),
    path('comments/create/', VideoCommentCreateAPI.as_view(), name='video_comment_create'),
    path('comments/', VideoCommentsListAPI.as_view(), name='video_comment_list'),
]