from django.urls import path
from .views import ListVideosAPI, UserVideosAPIView

urlpatterns = [
    path('', ListVideosAPI.as_view(), name='list_videos'),
    path('<slug>/', UserVideosAPIView.as_view(), name='list_user_videos')
]