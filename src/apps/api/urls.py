from os import name
from django.contrib import admin
from django.urls import path, include

from src.apps.api.views import upload_file_endpoit
from src.apps.api.views import login_user,signin_user, logout_user


urlpatterns = [
    path("uploader", upload_file_endpoit, name="uploader_api_method"),

    path("login",  login_user,  name="login_endpoint"),
    path("register", signin_user,  name="signin_endpoint"),
    # path("logout", logout_user, name="logout_endpoint")
]
 