from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify

class FilePathModel (models.Model):
    id              = models.AutoField      (primary_key=True)
    name            = models.CharField      (max_length=100, verbose_name="Filename")
    file            = models.FilePathField  (verbose_name="File Data")
    path_encoded    = models.CharField      (max_length=500, verbose_name="Encoded path")
    contenttype     = models.CharField      (max_length=100, verbose_name="Content Type")
    filesize        = models.IntegerField   (verbose_name="File Size")
    owner           = models.ForeignKey     (User, on_delete=models.CASCADE)
    created_at      = models.DateTimeField  (auto_now_add=True, verbose_name='Created at')
    updated_at      = models.DateTimeField  (auto_now=True,  verbose_name='Updated at')

    @property
    def slug_mtype (self):
        return slugify(self.contenttype.replace("/","-"))

    @property
    def file_path (self):
        return self.file.path

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'