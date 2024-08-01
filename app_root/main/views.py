from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()

    context = {
        "title": "Homey - Main page",
        "content": "HOMEY - Furniture Store",
        "categories": categories,
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Homey - About us",
        "content": "About us",
        "text_on_page": "Good stuff",
    }

    return render(request, "main/about.html", context)
