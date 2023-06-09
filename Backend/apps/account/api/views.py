from rest_framework.generics import ListAPIView
from apps.account.models import CustomUserModel
from .serializers import UserSerializer

class UserListAPIView(ListAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer