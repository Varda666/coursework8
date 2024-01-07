from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.user_role == 'moderator':
            return True
        return False


class IsOwnerOrPublic(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        elif obj.is_public is True:
            return obj
        else:
            return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        else:
            return False

