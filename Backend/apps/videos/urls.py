from django.urls import path
from .views import ListVideosAPI

urlpatterns = [
    path('', ListVideosAPI.as_view(), name='list_videos'),
]