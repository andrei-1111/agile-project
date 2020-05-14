import pytest

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient

from ..models import (
    Agile,
    Principle,
)


@pytest.fixture
def user():
    return User.objects.create_user('username', 'email@email.com', 'password',)


@pytest.fixture
def agile_value():
    return Agile.objects.create(
        name='Individuals and interactions over processes and tools',
        description='This value of the Agile manifesto focuses on giving importance',
    )


@pytest.fixture
def principle():
    return Principle.objects.create(
        name='Simplicity',
        description='Develop just enough to get the job done for right now',
    )


@pytest.fixture
def logged_in_client(user):
    """Setup a fixture for an APIClient with a logged in user."""
    client = APIClient()
    client.login(username=user.username, password='password')
    return client


@pytest.mark.django_db
class TestAgileValueViews:
    @pytest.fixture
    def defaults(self):
        payload = {
            'name': 'Working product over comprehensive documentation',
            'description': 'The Agile values dictate that the first and foremost duty',
        }
        return {
            'payload': payload,
        }

    def get_detail_url(self, value_id):
        return reverse('agile:agile-detail', args=[value_id])

    def test_unauthenticated_list_view(self, client):
        """Tests get request are allowed for unauthenticated Users."""
        url = reverse('agile:agile-list')
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_list_view(self, logged_in_client):
        url = reverse('agile:agile-list')
        resp = logged_in_client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_get_view(self, logged_in_client, agile_value):
        url = self.get_detail_url(agile_value.id)
        resp = logged_in_client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_unauthenticated_get_view(self, client, agile_value):
        """Tests get request are allowed for unauthenticated Users."""
        url = self.get_detail_url(agile_value.id)
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_unauthenticated_post(self, client, defaults):
        """Tests post request creates a Agile instance."""
        url = reverse('agile:agile-list')
        resp = client.post(url, defaults['payload'])
        assert resp.status_code == status.HTTP_403_FORBIDDEN

    def test_post(self, logged_in_client, defaults):
        """Tests post request creates a Value instance."""
        url = reverse('agile:agile-list')
        resp = logged_in_client.post(url, defaults['payload'])
        assert resp.status_code == status.HTTP_201_CREATED
        assert Agile.objects.filter(id=resp.json()['id']).exists() == True

    def test_unauthenticated_patch(self, client, agile_value, defaults):
        """Tests post request creates a Agile instance."""
        url = self.get_detail_url(agile_value.id)
        resp = client.patch(url, defaults['payload'])
        assert resp.status_code == status.HTTP_403_FORBIDDEN

    def test_patch(self, logged_in_client, agile_value):
        """Tests patch request updates the instance."""
        url = self.get_detail_url(agile_value.id)
        payload = {'description': 'New Description'}
        resp = logged_in_client.patch(url, payload)
        assert resp.status_code == status.HTTP_200_OK
        agile_value = Agile.objects.get(id=resp.json()['id'])
        assert agile_value.description == payload['description']

    def test_unauthenticated_put(self, client, agile_value, defaults):
        """Tests post request creates a Agile instance."""
        url = self.get_detail_url(agile_value.id)
        resp = client.put(url, defaults['payload'])
        assert resp.status_code == status.HTTP_403_FORBIDDEN

    def test_put(self, logged_in_client, agile_value):
        """Tests put request updates an instance."""
        url = self.get_detail_url(agile_value.id)
        payload = {'name': 'New Name', 'description': 'New Description'}
        resp = logged_in_client.put(url, payload)
        assert resp.status_code == status.HTTP_200_OK
        agile_value = Agile.objects.get(id=resp.json()['id'])
        assert agile_value.description == payload['description']
        assert agile_value.name == payload['name']


@pytest.mark.django_db
class TestPrincipleViews:
    @pytest.fixture
    def defaults(self):
        payload = {
            'name': 'Customer satisfaction through early and continuous software delivery',
            'description': 'Customers are happier when they receive working software',
        }
        return {
            'payload': payload,
        }

    def get_detail_url(self, principle_id):
        return reverse('agile:principle-detail', args=[principle_id])

    def test_unauthenticated_list_view(self, client):
        """Tests get request are allowed for unauthenticated Users."""
        url = reverse('agile:principle-list')
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_list_view(self, logged_in_client):
        url = reverse('agile:principle-list')
        resp = logged_in_client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_get_view(self, logged_in_client, principle):
        url = self.get_detail_url(principle.id)
        resp = logged_in_client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_unauthenticated_get_view(self, client, principle):
        """Tests get request are allowed for unauthenticated Users."""
        url = self.get_detail_url(principle.id)
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_unauthenticated_post(self, client, defaults):
        """Tests post request creates a Principle instance."""
        url = reverse('agile:principle-list')
        resp = client.post(url, defaults['payload'])
        assert resp.status_code == status.HTTP_403_FORBIDDEN

    def test_post(self, logged_in_client, defaults):
        """Tests post request creates a Principle instance."""
        url = reverse('agile:principle-list')
        resp = logged_in_client.post(url, defaults['payload'])
        assert resp.status_code == status.HTTP_201_CREATED
        assert Principle.objects.filter(id=resp.json()['id']).exists() == True

    def test_unauthenticated_patch(self, client, principle, defaults):
        """Tests post request creates a Principle instance."""
        url = self.get_detail_url(principle.id)
        resp = client.patch(url, defaults['payload'])
        assert resp.status_code == status.HTTP_403_FORBIDDEN

    def test_patch(self, logged_in_client, principle):
        """Tests patch request updates the instance."""
        url = self.get_detail_url(principle.id)
        payload = {'description': 'New Description'}
        resp = logged_in_client.patch(url, payload)
        assert resp.status_code == status.HTTP_200_OK
        principle = Principle.objects.get(id=resp.json()['id'])
        assert principle.description == payload['description']

    def test_unauthenticated_put(self, client, principle, defaults):
        """Tests post request creates a Principle instance."""
        url = self.get_detail_url(principle.id)
        resp = client.put(url, defaults['payload'])
        assert resp.status_code == status.HTTP_403_FORBIDDEN

    def test_put(self, logged_in_client, principle):
        """Tests put request updates an instance."""
        url = self.get_detail_url(principle.id)
        payload = {'name': 'New Name', 'description': 'New Description'}
        resp = logged_in_client.put(url, payload)
        assert resp.status_code == status.HTTP_200_OK
        principle = Principle.objects.get(id=resp.json()['id'])
        assert principle.description == payload['description']
        assert principle.name == payload['name']
