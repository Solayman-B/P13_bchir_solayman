from django.shortcuts import render
from .models import Letting


def index(request):
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    lettings = Letting.objects.get(id=letting_id)
    context = {
        "title": lettings.title,
        "address": lettings.address,
    }
    return render(request, "lettings/letting.html", context)
