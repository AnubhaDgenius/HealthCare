from rest_framework import permissions
class MyPers(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "OPTIONS"]:
            return True
        return request.user.is_superuser       
    
    def has_permission(self, request, view):
        if request.method in ["GET", "OPTIONS"]:
            return True
        return request.user.is_superuser    

class MyPers2(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "OPTIONS"]:
            return True
        return request.user.is_superuser or obj.user == request.user.id
