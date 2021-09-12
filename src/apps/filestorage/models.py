from django.db import models

from django.conf import settings
from django.contrib.auth.models import User

from src.apps.filestorage.handlers.storage_handler import SqliteStorageHandler


class FileStorageUserModel (models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    dbpath      = models.FileField(verbose_name="Database Path")

    created_at  = models.DateTimeField (auto_now_add=True, verbose_name='Created at')
    updated_at  = models.DateTimeField (auto_now=True, verbose_name='Updated at')

    def save(self, *args, **kwargs):
        sqmanager = SqliteStorageHandler()
        sqmanager.create_file()


        if not sqmanager.iserror:
            self.dbpath = sqmanager.finaldbpath
            
            print("User created")

            super(FileStorageUserModel, self).save(*args, **kwargs)