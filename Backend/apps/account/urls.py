from django.urls import path
from .views import UserListAPIView, UserDetailAPIView, ProfileAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('<slug>', UserDetailAPIView.as_view(), name='user_detail'),
    path('me/', ProfileAPIView.as_view(), name='me'),
]
