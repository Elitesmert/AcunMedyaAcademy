from rest_framework.permissions import DjangoModelPermissions
from rest_framework.exceptions import PermissionDenied


class CreateUserfulLinksPermission(DjangoModelPermissions):
    authenticated_users_only = True

    def has_permission(self, request, view):
        group_permissions = request.user.groups.permissions
        if request.user.is_authenticated and group_permissions.filter(codename='add_usefullinksmodel').exists():
            return True
        raise PermissionDenied("Bu sayfaya erişim için izniniz bulunmuyor!")
