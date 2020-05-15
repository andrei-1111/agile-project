from rest_framework import serializers

from .models import Agile


class AgileSerializer(serializers.ModelSerializer):
    """Serializer for Agile model."""

    class Meta:
        model = Agile
        fields = (
            'id',
            'type',
            'name',
            'description',
        )
