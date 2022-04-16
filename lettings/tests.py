import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db
def test_index():
    client = Client()

    path = reverse('lettings:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Lettings</title>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_lettings():
    client = Client()

    path = reverse('lettings:lettings/1/')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title></title>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")