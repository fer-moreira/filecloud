from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/',  admin.site.urls),
    path('api/v1/', include('src.apps.api.urls')),
    path('',        include('src.apps.frontend.urls'))
]
