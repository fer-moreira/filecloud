from base64 import encode
from typing import ForwardRef
from django.contrib.auth.models import User
from django.db.models.fields import FloatField
from src.apps.api.models import FilePathModel
from src.filecloud.encryption import EncryptionManager
import random
import pprint

def validated_register (POST_DATA):
    if "firstname"       in POST_DATA \
    and "secondname"     in POST_DATA \
    and "email"          in POST_DATA \
    and "password"       in POST_DATA \
    and "password2"      in POST_DATA \
    and "check_before_1" in POST_DATA \
    and "check_before_2" in POST_DATA:
        return True
    else:
        return False

def create_user (POST_DATA):
    try:
        randomurname = "%s_%s_%s_%s" %(
            random.getrandbits(40),
            POST_DATA.get("firstname")[0], 
            POST_DATA.get("secondname"),
            random.getrandbits(20),
        )

        new_user            = User()
        new_user.first_name = POST_DATA.get("firstname")
        new_user.last_name  = POST_DATA.get("secondname")
        new_user.email      = POST_DATA.get("email")
        new_user.username   = randomurname
        new_user.set_password(str(POST_DATA.get("password")))
        new_user.save()

        return new_user
    except:
        return None

def already_exists (POST_DATA):
    try:
        user = User.objects.filter(email=POST_DATA.get("email"))
        return user.exists()
    except Exception as r:
        raise




def save_file_to_db (payload):
    file = payload.get("file")
    path = payload.get("path")

    print(file.file)
    pprint.pprint(file.__dir__())

    file_in_db = FilePathModel()
    file_in_db.name = file.name
    file_in_db.file = path
    file_in_db.contenttype = file.content_type if file.content_type != "" else "unknown"
    file_in_db.filesize = file.size
    file_in_db.owner = payload.get("request").user

    strpath = path.__str__()
    encoded_path = EncryptionManager().encrypt(strpath)
    file_in_db.path_encoded = encoded_path

    file_in_db.save()