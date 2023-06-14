from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUserModel, CoursesModel
from .serializers import UserSerializer, ProfileSerializer, DepartmentSerializer, MyTokenObtainPairSerializer


class DepartmentsListAPI(ListAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = DepartmentSerializer


class UserListAPIView(ListAPIView):
    queryset = CustomUserModel.objects.filter(groups=1)
    serializer_class = UserSerializer


class InstructorListAPI(ListAPIView):
    queryset = CustomUserModel.objects.filter(groups=2)
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


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
