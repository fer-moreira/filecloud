from django.contrib import admin

from src.apps.api.models import ContentTypeModels



admin.site.site_header = "Filecloud"
admin.site.site_title = "Filecloud"
admin.site.index_title = "Administration"

# Register your models here.
@admin.register(ContentTypeModels)
class ContentTypeModelAdmin (admin.ModelAdmin):
    search_fields = ('name','contenttype')
    list_filter = ('name','contenttype')
    list_display = ('svgcontent', 'name', 'contenttype','updated_at', 'created_at')