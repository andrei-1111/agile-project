import pytest

from django.test import TestCase

from ..models import (
    Agile,
    Principle,
)
from ..serializers import (
    AgileValueSerializer,
    AgilePrincipleSerializer,
)


@pytest.mark.django_db
class TestAgileSerializer:
    @pytest.fixture
    def agile_fixture(self, db):
        return Agile.objects.create(name='name', description='description')

    @pytest.fixture
    def defaults(self, agile_fixture):
        data = {
            'name': 'name',
            'description': 'description',
        }
        return {
            'page': agile_fixture,
            'data': data,
        }

    def test_valid(self, defaults):
        serializer = AgileValueSerializer(data=defaults['data'])
        assert serializer.is_valid() == True

    def test_save(self, defaults):
        serializer = AgileValueSerializer(data=defaults['data'])
        serializer.is_valid()
        instance = serializer.save()
        assert instance.name == defaults['data']['name']
        assert instance.description == defaults['data']['description']


@pytest.mark.django_db
class TestAgilePrincipleSerializer:
    @pytest.fixture
    def agile_fixture(self, db):
        return Principle.objects.create(name='name', description='description')

    @pytest.fixture
    def defaults(self, agile_fixture):
        data = {'name': 'name', 'description': 'description'}
        return {'page': agile_fixture, 'data': data}

    def test_valid(self, defaults):
        serializer = AgilePrincipleSerializer(data=defaults['data'])
        assert serializer.is_valid() == True

    def test_save(self, defaults):
        serializer = AgilePrincipleSerializer(data=defaults['data'])
        serializer.is_valid()
        instance = serializer.save()
        assert instance.name == defaults['data']['name']
        assert instance.description == defaults['data']['description']
