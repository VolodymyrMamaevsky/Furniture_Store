from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context: dict = {"title": "Home", "content": "Store main page"}

    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    return HttpResponse("About")
