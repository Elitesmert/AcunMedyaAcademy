from django.contrib.auth.backends import ModelBackend
from .models import CustomUserModel


class CustomUserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUserModel.objects.get(username=username)
            if user.check_password(password):
                return user
        except CustomUserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUserModel.objects.get(pk=user_id)
        except CustomUserModel.DoesNotExist:
            return None
