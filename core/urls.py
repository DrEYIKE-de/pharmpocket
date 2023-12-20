from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("secret/", admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "Pharm_Pocket"
admin.site.site_header = "PharmPocket Portal"
admin.site.index_title = "Welcome to PharmPocket administration"