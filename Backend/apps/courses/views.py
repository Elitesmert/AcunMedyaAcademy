from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, \
    get_object_or_404, RetrieveAPIView
from .models import CoursesModel
from .serializers import CoursesSerializer


class CourseListAPI(ListAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer


class CourseCreateAPI(CreateAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer
