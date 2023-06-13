from django.urls import path, include
from .account.views import InstructorListAPI, DepartmentsListAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', include('apps.account.urls')),
    path('useful-links/', include('apps.useful_links.urls')),
    path('videos/', include('apps.videos.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('teachers/', InstructorListAPI.as_view(), name='instructor_list'),
    path('departments/', DepartmentsListAPI.as_view(), name='department_list'),
]