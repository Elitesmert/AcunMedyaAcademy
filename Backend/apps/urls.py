from django.urls import path, include
from .account.views import InstructorListAPI, CoursesListAPI, MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', include('apps.account.urls')),
    path('useful-links/', include('apps.useful_links.urls')),
    path('videos/', include('apps.videos.urls')),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('instructors/', InstructorListAPI.as_view(), name='instructor_list'),
    path('courses/', CoursesListAPI.as_view(), name='department_list'),
]