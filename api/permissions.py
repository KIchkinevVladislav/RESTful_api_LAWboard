from rest_framework import permissions


class OwnResoursePermission(permissions.BasePermission):
    message = 'Это действие для Вас невозможно'

    def has_object_permission(self, request, view, obj):
        if request.method in ('POST', 'DELETE', 'PUT', 'PATCH'):
            return request.user == obj.author 
        return True  
