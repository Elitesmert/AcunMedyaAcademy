from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, get_object_or_404, RetrieveAPIView
from .models import VideoModel, VideoCommentModel
from ..account.models import CustomUserModel
from rest_framework.permissions import IsAuthenticated
from .serializers import VideosSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ListVideosAPI(ListAPIView):
    queryset = VideoModel.objects.all()
    serializer_class = VideosSerializer
    permission_classes = [IsAuthenticated]


class UserVideosAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self, user):
        # Kullanıcının videolarını döndüren bir queryset oluşturun
        return VideoModel.objects.filter(instructor=user)

    def get(self, request, slug):
        # Kullanıcıyı slug'a göre alın
        user = get_object_or_404(CustomUserModel, slug=slug)


        # Kullanıcının videolarının queryset'ini alın
        queryset = self.get_queryset(user)

        # Videoları serialize edin
        serializer = VideosSerializer(queryset, many=True)
        return Response(serializer.data)
