from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    message = 'Kirish taqiqlanadi.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user