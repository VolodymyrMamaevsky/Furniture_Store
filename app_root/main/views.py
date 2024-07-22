from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context: dict = {
        "title": "Homey - Main page",
        "content": "HOMEY - Furniture Store",
    }

    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    context: dict = {
        "title": "Homey - About us",
        "content": "About us",
        "text_on_page": "Good stuff",
    }

    return render(request, "main/about.html", context)
