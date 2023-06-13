from rest_framework.permissions import DjangoModelPermissions, BasePermission
from rest_framework.exceptions import PermissionDenied


class CreateVideosPermission(DjangoModelPermissions):
    authenticated_users_only = True

    def has_permission(self, request, view):
        group_permissions = request.user.groups.permissions
        if request.user.is_superuser or group_permissions.filter(codename='add_videosmodel').exists():
            return True
        raise PermissionDenied("Bu sayfaya erişim için izniniz bulunmuyor!")


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user or request.user.is_superuser:
            return True
        raise PermissionDenied("Başkasının eklediği link üzerinde işlem yapamazsınız!")
