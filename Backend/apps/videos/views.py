from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import VideoModel, VideoCommentModel
from rest_framework.permissions import IsAuthenticated


class ListVideosAPI(ListAPIView):
    queryset = VideoModel.objects.all()
    permission_classes = [IsAuthenticated]
