from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import VideoModel, VideoCommentModel
from rest_framework.permissions import IsAuthenticated
from .serializers import VideosSerializer


class ListVideosAPI(ListAPIView):
    queryset = VideoModel.objects.all()
    serializer_class = VideosSerializer
    permission_classes = [IsAuthenticated]
