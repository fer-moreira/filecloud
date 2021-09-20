from os import name
from django.contrib import admin
from django.urls import path, include

from src.apps.api.views import (
    upload_file_endpoit, 
    create_folder_endpoint,
    delete_file_endpoint
)
from src.apps.api.views import login_user,signin_user, logout_user


urlpatterns = [
    path("uploader",    upload_file_endpoit,    name="uploader_api_method"),
    path("new-folder",  create_folder_endpoint, name="folder_api_method"),
    path("delete",      delete_file_endpoint, name="delete_api_method"),

    path("login",  login_user,  name="login_endpoint"),
    path("register", signin_user,  name="signin_endpoint"),
    # path("logout", logout_user, name="logout_endpoint")
]
 