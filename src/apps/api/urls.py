from django.contrib import admin
from django.urls import path, include
from src.apps.api.views import proto_uploader

urlpatterns = [
    path("uploader", proto_uploader, name="uploader_api_method")
]
