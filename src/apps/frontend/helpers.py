from django.conf import settings

from src.apps.api.models import FilePathModel
from src.filecloud.encryption import EncryptionManager

import os


class DriveManager (object):
    def __init__ (self):
        self.root_path = settings.FINAL_FILES_PATH

    def get_files_object (self, selected_path, decrypt=False):
        decrypted_path = None

        if not decrypt: decrypted_path = selected_path
        else: decrypted_path = self.decrypt_path(selected_path)

        files_in_path = os.listdir(decrypted_path)

        wpath_files = [decrypted_path / x for x in files_in_path]

        wpath_objects = []

        for obj_path in wpath_files:
            if os.path.isfile(obj_path):
                obj_model = FilePathModel.objects.filter(file=obj_path)
                if obj_model.exists():
                    wpath_objects.append(obj_model[0])
                else:
                    print("file not found in database, but exists in drive")
            else:
                print("handle directory")

        return wpath_objects

    def decrypt_path (self, path):
        return EncryptionManager().decrypt(path)

    def encrypt_path (self, path):
        return EncryptionManager().encrypt(path)