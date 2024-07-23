from django.contrib import admin
from django.urls import path

from app_root.main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
]
