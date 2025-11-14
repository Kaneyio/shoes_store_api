import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.fixture
def api_client(db):
    User = get_user_model()
    user = User.objects.create_user(username="test", password="123")
    client = APIClient()
    client.force_authenticate(user)
    return client