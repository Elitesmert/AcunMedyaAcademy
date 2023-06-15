from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, \
    get_object_or_404, RetrieveAPIView
from .models import VideoModel, VideoCommentModel
from ..account.models import CustomUserModel
from rest_framework.permissions import IsAuthenticated
from .serializers import VideosSerializer, VideoCreateUpdateSerializer, VideoCommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import CreateVideosPermission, UpdateVideosPermission, DeleteVideosPermission, IsOwner


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


class VideoDetailAPI(RetrieveAPIView):
    serializer_class = VideosSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def get_object(self):
        slug = self.kwargs['slug']
        video = get_object_or_404(VideoModel, slug=slug)
        return video

    def get_queryset(self):
        return VideoModel.objects.all()


class VideoCreateAPI(CreateAPIView):
    queryset = VideoModel.objects.all()
    serializer_class = VideoCreateUpdateSerializer
    permission_classes = [IsAuthenticated, CreateVideosPermission]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)


class VideoUpdateAPI(RetrieveUpdateAPIView):
    queryset = VideoModel.objects.all()
    serializer_class = VideoCreateUpdateSerializer
    permission_classes = [IsAuthenticated, UpdateVideosPermission, IsOwner]
    lookup_field = 'slug'


class VideoDeleteAPI(DestroyAPIView):
    queryset = VideoModel.objects.all()
    serializer_class = VideosSerializer
    permission_classes = [IsAuthenticated, DeleteVideosPermission, IsOwner]


class VideoCommentCreateAPI(CreateAPIView):
    queryset = VideoCommentModel.objects.all()
    serializer_class = VideoCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class VideoCommentsListAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoCommentSerializer

    def get_queryset(self):
        return VideoCommentModel.objects.filter(parent=None)
