from rest_framework import (
    permissions,
    viewsets,
)

from .models import Agile
from .serializers import AgileSerializer


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj) -> bool:
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only Authenticated Users allowed
        return request.user and request.user.is_authenticated


class AgileViewSet(viewsets.ModelViewSet):
    queryset = Agile.objects.all()
    serializer_class = AgileSerializer
    permission_classes = (IsAuthenticated,)
