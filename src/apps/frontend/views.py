from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from src.filecloud.encryption import EncryptionManager
from src.apps.frontend.helpers import DriveManager, beautify_path
from pathlib import Path
import json

ERRORS_MAP = settings.ERRORS_MAP

class FolderEncryptView (TemplateView):
    template_name = "pages/main.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if not request.user.is_authenticated:
            return redirect(reverse("front_login"))

        request_path = request.GET.get("target")
        target_folder = EncryptionManager().decrypt(request_path)

        target_path = Path(target_folder)

        files_obj =  self.get_files(target_path)
        context["items"] = files_obj


        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(FolderEncryptView, self).get_context_data(**kwargs)
        context["breadcrumb"] = beautify_path(self.request.GET.get("target"))
        return context
    
    def get_files (self, target_path):
        files_items = DriveManager().get_files_object(target_path, False)
        return files_items


class PublicDriveView (TemplateView):
    template_name = "pages/main.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if not request.user.is_authenticated:
            return redirect(reverse("front_login"))

        files_obj =  self.get_files()
        context["items"] = files_obj

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(PublicDriveView, self).get_context_data(**kwargs)
        context["breadcrumb"] = ["Public"]
        return context

    def get_files (self):
        files_items = DriveManager().get_files_object(settings.HOME_FILES_PATH, False)
        return files_items


class LoginView (TemplateView):
    template_name = "pages/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)

        GET_DATA = self.request.GET

        if "error" in GET_DATA:
            error_id = int(GET_DATA.get("error"))
            error_description = ERRORS_MAP.get(error_id)

            context['hasError'] = True
            context['errorDescription'] = error_description
        else:
            context['hasError'] = False

        return context

class RegisterView (TemplateView):
    template_name = "pages/register.html"

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        
        GET_DATA = self.request.GET

        if "error" in GET_DATA:
            error_id = int(GET_DATA.get("error"))
            error_description = ERRORS_MAP.get(error_id)

            context['hasError'] = True
            context['errorDescription'] = error_description
        else:
            context['hasError'] = False

        return context
