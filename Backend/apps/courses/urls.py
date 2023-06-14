from django.urls import path
from .views import CourseListAPI, CourseCreateAPI

urlpatterns = [
    path('', CourseListAPI.as_view(), name='courses_list'),
    path('create/', CourseCreateAPI.as_view(), name='courses_list'),
]