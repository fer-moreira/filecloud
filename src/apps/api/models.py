from os import name
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class ContentTypeModels (models.Model):
    id          = models.AutoField      (primary_key=True)
    name        = models.CharField      (max_length=10, verbose_name="SVG File Name")
    contenttype = models.CharField      (max_length=50, verbose_name="Content Type")
    svgfile     = models.FileField      (verbose_name="SVG File Icon", upload_to='contentypes/' )
    created_at  = models.DateTimeField  (auto_now_add=True, verbose_name='Created at')
    updated_at  = models.DateTimeField  (auto_now=True, verbose_name='Updated at')

    def svg_file_path (self):
        return self.svgfile.path

    def svg_file_url (self):
        return self.svgfile.url

    def svgcontent (self):
        _file = self.svgfile.open("r")
        _content = _file.readline()
        _file.close()

        return mark_safe(str(_content))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContentType Icon'
        verbose_name_plural = 'ContentType Icons'