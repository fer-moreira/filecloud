#usr

from src.filecloud.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database/db.sqlite3',
    }
}
