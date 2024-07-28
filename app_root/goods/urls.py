from django.contrib import admin
from django.urls import path

from app_root.goods import views

app_name = "goods"

urlpatterns = [
    path("", views.catalog, name="index"),
    path("product/", views.product, name="product"),
]
