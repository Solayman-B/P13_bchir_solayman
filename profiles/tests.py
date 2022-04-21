import pytest

from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from .models import Profile


@pytest.mark.django_db
def test_index():
    client = Client()

    path = reverse("profiles:index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Profiles</title>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profiles():
    client = Client()

    user_1 = User.objects.create_user(
        username="test_username",
        email="test@gmail.com",
        password="password",
    )
    Profile.objects.create(user=user_1, favorite_city="Paris")
    path = reverse("profiles:profile", kwargs={"username": user_1.username})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>test_username</title>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
