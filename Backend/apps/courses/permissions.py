from rest_framework.permissions import DjangoModelPermissions
from rest_framework.exceptions import PermissionDenied


class CreateCoursePermission(DjangoModelPermissions):
    authenticated_users_only = True

    def has_permission(self, request, view):
        if request.user.groups:
            group_permissions = request.user.groups.permissions
            if request.user.is_superuser or group_permissions.filter(codename='add_coursesmodel').exists():
                return True
            raise PermissionDenied("Bu sayfaya erişim için izniniz bulunmuyor!")
        else:
            raise PermissionDenied("Kaydınızda grubunuz belirtilmemiş, lütfen yetkili birimlere bildiriniz!")
