from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import (
    AgilePrincipleViewSet,
    AgileValueViewSet,
)

app_name = 'agile'


router = DefaultRouter()
router.register('agile-values', AgileValueViewSet)
router.register('agile-principles', AgilePrincipleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
