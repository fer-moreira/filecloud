from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save

from src.apps.filestorage.models import FileStorageUserModel


@receiver(post_save, sender=User)
def create_user_db(sender, instance, created, **kwargs):
    print("sender postsave user")
    if created:
        print("usuario criado")
        FileStorageUserModel.objects.create(user=instance)
