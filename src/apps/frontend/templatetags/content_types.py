from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()



MIMEMAPPING = {
    "folder" : "folder-public.svg",
    "folder-private" : "folder-locked.svg",
    "generic" : "app-common.svg",

    "audio/mpeg" : "app-media.svg",
    "application/ogg" : "app-media.svg",
    "audio/ogg" : "app-media.svg",
    "video/ogg" : "app-media.svg",
    
    "coding" : "app-code_2.svg",
    "text-x-python" : "app-code_3.svg",
    "application/octet-stream" : "app-code_3.svg",

    "application/zip" : "app-zip.svg",
    "application/vnd.rar" : "app-zip.svg",
    "application/x-7z-compressed" : "app-zip.svg",
    
    "image/png" : "app-image.svg",
    "image/jpeg" : "app-image.svg",
    "image/jpg" : "app-image.svg",
    "image/bpm" : "app-image.svg",
    "image/bitmap" : "app-image.svg",
    "image/pdf" : "app-image.svg",
    "application/pdf" : "app-image.svg",

    "text/x-yaml" : "app-json.svg",
    "text/yaml" : "app-json.svg",
    "text/yml" : "app-json.svg",
    "application/json" : "app-json.svg",
    "application/ini" : "app-json.svg",
    "application/x-yaml" : "app-json.svg",
    "application/x-yml" : "app-json.svg",
    "application/yaml" : "app-json.svg",
    "application/yml" : "app-json.svg",

}


@register.simple_tag(name="get_icon")
def get_icon (value):
    available_types = MIMEMAPPING.keys()
    content_type = str(value) if value in available_types else "generic"
    
    TYPE_SVG_NAME = MIMEMAPPING.get(content_type)
    svg_path = (settings.MIMETYPES_FOLDER / TYPE_SVG_NAME)
    
    svg_file = open(svg_path, "r")
    svg_content = svg_file.read()
    svg_file.close()

    return mark_safe(svg_content)