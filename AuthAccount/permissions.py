from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False
class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user.is_admin:
            return account == request.user
        return False