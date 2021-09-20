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

        wpath_files.sort(key=lambda x: os.path.getmtime(x))
        wpath_files = reversed(wpath_files)

        wpath_objects = []
        wdir_objects = []

        for obj_path in wpath_files:
            if os.path.isfile(obj_path):
                model = self.try_get_object(obj_path)
                
                wpath_objects.append(model[0]) \
                    if model.exists() \
                        else \
                            print("file not found in database, but exists in drive:\n[%s]" %obj_path)

            elif os.path.isdir(obj_path):
                model = self.try_get_object(obj_path)
                
                wdir_objects.append(model[0]) \
                    if model.exists() \
                        else \
                            print("Directory not found in database, but exists in drive:\n[%s]" %obj_path)
                
            else:
                print("handle other file type")

        
        return list(wdir_objects + wpath_objects)

    def decrypt_path (self, path):
        return EncryptionManager().decrypt(path)

    def encrypt_path (self, path):
        return EncryptionManager().encrypt(path)

    def try_get_object (self, objpath):
        return  FilePathModel.objects.filter(file=objpath).order_by("-created_at")

def beautify_path (path):
    sh = settings.HOME_FILES_PATH
    h = sh.__str__()
    p = EncryptionManager().decrypt(path)
    final = p.replace(h,"").split("\\")
    return final[1:]