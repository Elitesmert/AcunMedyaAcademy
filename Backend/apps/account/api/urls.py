from django.urls import path
from .views import UserListAPIView

urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='user_list'),
]
