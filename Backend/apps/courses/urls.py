from django.urls import path
from .views import CourseListAPI, CourseCreateAPI, CourseUpdateAPI, CourseDeleteAPI

urlpatterns = [
    path('', CourseListAPI.as_view(), name='courses_list'),
    path('create/', CourseCreateAPI.as_view(), name='course_create'),
    path('update/<slug>', CourseUpdateAPI.as_view(), name='course_update'),
    path('delete/<slug>', CourseDeleteAPI.as_view(), name='course_delete'),
]