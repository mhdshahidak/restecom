from rest_framework import permissions



class BasicUserPermission(permissions.BasePermission):
     def has_permission(self, request, view):
        if request.user.is_authenticated or request.user.is_superuser:
            return True