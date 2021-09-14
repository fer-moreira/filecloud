from django.contrib import admin
from django.urls import path, include
# from src.apps.frontend.views import HomepageView

from src.apps.filestorage.views import HomepageView

urlpatterns = [
    path("", HomepageView.as_view(), name="front_homepage")
]