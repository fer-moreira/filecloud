from django.contrib import admin
from src.apps.filestorage.models import FileStorageUserModel

# Register your models here.
@admin.register(FileStorageUserModel)
class ContentTypeModelAdmin (admin.ModelAdmin):
    list_display = ('dbpath',)