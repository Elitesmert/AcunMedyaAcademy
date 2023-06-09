from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import CustomUserModel, DepartmentModel
from .serializers import UserSerializer, ProfileSerializer


class UserListAPIView(ListAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'slug'

    def get_object(self):
        slug = self.kwargs['slug']
        user = get_object_or_404(CustomUserModel, slug=slug)
        return user

    def get_queryset(self):
        return CustomUserModel.objects.all()


class ProfileAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = CustomUserModel.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

