from os import stat_result
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.conf import settings
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.urls import reverse
from django.shortcuts import redirect
from pathlib import Path
from src.apps.api.models import FilePathModel
from src.filecloud.encryption import EncryptionManager

from src.apps.api.helpers import (
    already_exists, 
    create_user, 
    validated_register,
    save_file_to_db,
    create_folder_in_db
)

@csrf_protect
def delete_file_endpoint (request):
    if request.method.upper() == "POST":
        if request.user.is_authenticated:
            POST_DATA = request.POST
            target_file = POST_DATA.get("delete_target")

            try:
                file_obj = FilePathModel.objects.get(path_encoded=target_file)
                file_obj.delete()
                return HttpResponse("Ok", status=200)
            except FilePathModel.DoesNotExist as r:
                return HttpResponse("Path Does not Exists", status=200)

        else:
            return HttpResponse("Forbidden!", status=403)
    else:
        return HttpResponse("%s" %request.method, status=405)

@csrf_protect
def create_folder_endpoint (request):
    if request.method.upper() == "POST":
        try:
            POST_DATA   = request.POST
            folder_name = POST_DATA.get("new_folder_name");
            target      = POST_DATA.get("target")
            target_decrypt = None

            if target != "public":
                print("decrypt")
                target_decrypt = EncryptionManager().decrypt(target);
            else:
                print("ispublic")
                target_decrypt = settings.HOME_FILES_PATH.__str__()
            
            try:
                create_folder_in_db({
                    "request" : request,
                    "name" : folder_name,
                    "path" : target_decrypt
                });

                return HttpResponse("Folder created", status=200);

            except Exception as r:
                raise
                return HttpResponse("Error when creating folder", status=500)
        except Exception as r:
            raise
            return HttpResponse("Error when receiving the FormData, verify the calls in javascript", status=500)

    else:
        logout(request)

@csrf_protect
def upload_file_endpoit (request):
    if request.method.upper() == "POST":
        file = request.FILES['file'] if 'file' in request.FILES else None
        file_content = ContentFile(file.read())
        fout_path = ""

        if str(request.POST.get("target")) == "public":
            fout_path = settings.FINAL_FILES_PATH / file.name
        else:
            request_path = str(request.POST.get("target"))
            decrypt_path = EncryptionManager().decrypt(request_path)
            fout_path = Path(decrypt_path) / file.name


        fout = open(fout_path, "wb+")

        try:
            for chunk in file_content.chunks(): fout.write(chunk)
            fout.close()

            try:
                save_file_to_db({
                    "request" : request,
                    "file" : file,
                    "path" : fout_path
                })
            except Exception as r:
                return HttpResponse("Error when saving file to system", status=500)
                
            return HttpResponse("OK", status=200)
        except Exception as r:
            fout.close()
            return HttpResponse("Internal Server Error", status=500)
        
    elif request.method.upper() == "GET":
        return HttpResponse("I'm a teapot ?", status=418)
    else:
        return HttpResponse("Forbidden", status=403)

@csrf_protect
def login_user (request):
    if request.method.upper() == "POST":
        POST_DATA = request.POST

        if "email" in POST_DATA and "password" in POST_DATA:
            try:
                user = User.objects.get(email=POST_DATA.get("email"))

                if user.check_password(POST_DATA.get("password")):
                    login(request, user)
                    return redirect(reverse("front_homepage"))
                else:
                    return redirect("/login?error=101")

            except User.DoesNotExist as r:
                return redirect("/login?error=202")

@csrf_protect
def signin_user (request):
    if request.method.upper() == "POST":
        POST_DATA = request.POST
        
        try:
            is_valid_data = validated_register(POST_DATA)

            if already_exists(POST_DATA): return redirect("/register?error=306")
            if not is_valid_data:         return redirect("/register?error=303")
            else:
                if not POST_DATA.get("password") == POST_DATA.get("password2"):
                    return redirect("/register?error=304")
                else: 
                    user_created = create_user(POST_DATA)
                    if user_created: return redirect(reverse("front_login"))
                    else:            return redirect("/register?error=305")

        except: return redirect("/register?error=305")
    else: return redirect(reverse("front_register"))

@csrf_exempt
def logout_user (request):
    logout(request)
    return redirect(reverse("front_login"))
