from rest_framework import permissions

class IsActivityOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an activity to view or edit it.
    """
    def has_object_permission(self, request, view, obj):
        # The activity user must match the requesting authenticated user
        return obj.user == request.user