from rest_framework.permissions import BasePermission
from rest_framework_api_key.permissions import HasAPIKey


class IsAdminOrHasAPIKey(BasePermission):
    def has_permission(self, request, view):
        is_admin = (
            request.user and request.user.is_authenticated and request.user.is_staff
        )
        has_api_key = HasAPIKey().has_permission(request, view)
        return is_admin or has_api_key
