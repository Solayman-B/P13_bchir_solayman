import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

def test_index():
    client = Client()

    path = reverse('index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Holiday Homes</title>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")



def test_dummy():
    assert 1
