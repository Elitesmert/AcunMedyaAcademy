from rest_framework.permissions import DjangoModelPermissions
from rest_framework.exceptions import PermissionDenied


class CreateCoursePermission(DjangoModelPermissions):
    authenticated_users_only = True

    def has_permission(self, request, view):
        if request.user.groups:
            group_permissions = request.user.groups.permissions
            if request.user.is_superuser or group_permissions.filter(codename='add_coursesmodel').exists():
                return True
            raise PermissionDenied("Kurs ekleme yetkisine sahip değilsiniz!")
        else:
            raise PermissionDenied("Kaydınızda grubunuz belirtilmemiş, lütfen yetkili birimlere bildiriniz!")


class DeleteCoursePermission(DjangoModelPermissions):
    authenticated_users_only = True

    def has_permission(self, request, view):
        if request.user.groups:
            group_permissions = request.user.groups.permissions
            if request.user.is_superuser or group_permissions.filter(codename='delete_coursesmodel').exists():
                return True
            raise PermissionDenied("Kurs silme yetkisine sahip değilsiniz!")
        else:
            raise PermissionDenied("Kaydınızda grubunuz belirtilmemiş, lütfen yetkili birimlere bildiriniz!")


class UpdateCoursePermission(DjangoModelPermissions):
    authenticated_users_only = True

    def has_permission(self, request, view):
        if request.user.groups:
            group_permissions = request.user.groups.permissions
            if request.user.is_superuser or group_permissions.filter(codename='change_coursesmodel').exists():
                return True
            raise PermissionDenied("Kurs düzenleme yetkisine sahip değilsiniz!")
        else:
            raise PermissionDenied("Kaydınızda grubunuz belirtilmemiş, lütfen yetkili birimlere bildiriniz!")
