from rest_framework import permissions




class IsOwnerOrReadOnly(permissions.BasePermission):

    """
    This class grants only the owners of drugs to be able to delete or them.
    It is read only for others.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user

