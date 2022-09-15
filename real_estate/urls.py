import imp
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('supersecret/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header='PETR Estate admin'
admin.site.site_title='PETR Real Estate Admin Portal'
admin.site.index_title='Welcome to the PETR Real Estate Protal'
