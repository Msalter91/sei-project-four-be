from rest_framework import permissions

class isOwnerOrReadyOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, _view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user