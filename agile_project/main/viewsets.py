from rest_framework import viewsets

from .models import (
    Agile,
    Principle,
)
from .serializers import (
    AgilePrincipleSerializer,
    AgileValueSerializer,
)


class AgilePrincipleViewSet(viewsets.ModelViewSet):
    queryset = Principle.objects.all()
    serializer_class = AgilePrincipleSerializer


class AgileValueViewSet(viewsets.ModelViewSet):
    queryset = Agile.objects.all()
    serializer_class = AgileValueSerializer
