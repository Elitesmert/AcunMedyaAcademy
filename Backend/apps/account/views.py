from rest_framework.generics import ListAPIView
from .models import CustomUserModel, DepartmentModel
from .serializers import UserSerializer

class UserListAPIView(ListAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer

class DepartmentListAPIView(ListAPIView):
    queryset = DepartmentModel.objects.all()