from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, \
    get_object_or_404, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import CoursesModel
from .serializers import CoursesSerializer
from .permissions import CreateCoursePermission, DeleteCoursePermission, UpdateCoursePermission


class CourseListAPI(ListAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer


class CourseCreateAPI(CreateAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticated, CreateCoursePermission]


class CourseUpdateAPI(RetrieveUpdateAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, UpdateCoursePermission]


class CourseDeleteAPI(DestroyAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, DeleteCoursePermission]
