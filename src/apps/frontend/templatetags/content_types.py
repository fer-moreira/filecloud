from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
import yaml

register = template.Library()

mimemapping_path = settings.BASE_DIR / "settings/mimemapping.yaml"
mimemap_file = mimemapping_path.open()
mimemap_content = mimemap_file.read()
mimemap_file.close()

MIMEMAPPING = yaml.load(mimemap_content, Loader=yaml.FullLoader)


@register.simple_tag(name="get_icon")
def get_icon (value):
    mime_found = False
    current_mime = "app-common.svg"

    for mime in MIMEMAPPING:
        valid_types = MIMEMAPPING.get(mime)
        
        if value in valid_types:
            mime_found = True
            current_mime = mime
            break

    mime_file = (settings.MIMETYPES_FOLDER / current_mime).open("r")
    mime_content = mime_file.read()
    mime_file.close()

    return mark_safe(mime_content)