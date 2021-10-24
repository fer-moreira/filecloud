from os import name
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include

from src.apps.frontend.views import FolderEncryptView, PublicDriveView, LoginView, RegisterView
from src.apps.api.views import logout_user

from django.http import HttpResponse
from django.template import loader


urlpatterns = [
    path("folder",              FolderEncryptView.as_view(), name="front_homepage"),
    path("folder/public-drive", PublicDriveView.as_view(), name="front_homepage"),

    # LOGIN PAGE
    path("login",    LoginView.as_view(),    name="front_login"),
    path("register", RegisterView.as_view(), name="front_register"),
    path("logout",   logout_user,            name="front_logout"),
    path("forgot",   logout_user,            name="front_forgot")
]
