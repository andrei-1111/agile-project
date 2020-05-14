from rest_framework import (
    permissions,
    viewsets,
)

from .models import (
    Agile,
    Principle,
)
from .serializers import (
    AgilePrincipleSerializer,
    AgileValueSerializer,
)


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only Authenticated Users allowed
        return request.user and request.user.is_authenticated


class AgilePrincipleViewSet(viewsets.ModelViewSet):
    queryset = Principle.objects.all()
    serializer_class = AgilePrincipleSerializer
    permission_classes = (IsAuthenticated,)


class AgileValueViewSet(viewsets.ModelViewSet):
    queryset = Agile.objects.all()
    serializer_class = AgileValueSerializer
    permission_classes = (IsAuthenticated,)
