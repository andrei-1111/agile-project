from rest_framework import (
    serializers,
)

from .models import (
    Agile,
    Principle,
)


class AgileValueSerializer(serializers.ModelSerializer):
    """Serializer for Agile model."""

    class Meta:
        model = Agile
        fields = (
            'id',
            'name',
            'description',
        )


class AgilePrincipleSerializer(serializers.ModelSerializer):
    """Serializer for Principle model."""

    class Meta:
        model = Principle
        fields = (
            'id',
            'name',
            'description',
        )
