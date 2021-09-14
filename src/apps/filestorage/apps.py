from django.apps import AppConfig


class FilestorageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.apps.filestorage'

    def ready (self):
        import src.apps.filestorage.signals