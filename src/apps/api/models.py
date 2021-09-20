from src.filecloud.encryption import EncryptionManager
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from pathlib import Path
import os, shutil

class FilePathModel (models.Model):
    id              = models.AutoField      (primary_key=True)
    name            = models.CharField      (max_length=100, verbose_name="Filename")
    file            = models.FilePathField  (verbose_name="File Data")
    path_encoded    = models.CharField      (max_length=500, verbose_name="Encoded path")
    contenttype     = models.CharField      (max_length=100, verbose_name="Content Type")
    owner           = models.ForeignKey     (User, on_delete=models.CASCADE)
    created_at      = models.DateTimeField  (auto_now_add=True, verbose_name='Created at')
    updated_at      = models.DateTimeField  (auto_now=True,  verbose_name='Updated at')

    @property
    def filesize (self):
        if self.is_file:
            return os.path.getsize(self.file)
        else:
            return sum(os.path.getsize(Path(self.file) / f) for f in os.listdir(self.file) if os.path.isdir(self.file))

    @property
    def slug_mtype (self):
        return slugify(self.contenttype.replace("/","-"))

    @property
    def file_path (self):
        return self.file.path

    @property
    def human_type (self):
        if self.contenttype == "folder":  return "folder"
        if not "." in self.name: return "binary"
        else: return self.name.split(".")[-1]
        
    @property
    def owner_name (self):
        return self.owner.username if self.owner.first_name == '' else self.owner.username

    @property
    def is_file (self):
        return os.path.isfile(self.file)
    
    @property
    def is_dir (self):
        return os.path.isdir(self.file)

    @property
    def type_href (self):
        return "folder" if self.is_dir else "file"

    @property
    def data_loc (self):
        return "_blank" if self.is_file else "_self"

    @property
    def data_href (self):
        return '%s' % (self.path_encoded)

    def delete(self):
        if os.path.exists(self.file): 
            if os.path.isdir(self.file):
                shutil.rmtree(self.file)
            else:
                os.remove(self.file)

        super(FilePathModel, self).delete()

    def rename (self, newname):
        fpath = self.file
        npath = fpath.replace(self.name, newname)
        os.rename(fpath, npath)
        self.file = npath
        self.name = newname
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'