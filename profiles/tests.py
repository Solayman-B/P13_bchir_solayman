import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db
def test_index():
    client = Client()

    path = reverse('profiles:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Profiles</title>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")