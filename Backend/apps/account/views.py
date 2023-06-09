from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from .models import CustomUserModel, DepartmentModel
from .serializers import UserSerializer


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
