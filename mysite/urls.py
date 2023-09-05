from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from filebrowser.sites import site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('blog.urls')),
    path('admin/filebrowser/', site.urls),
    path('tinymce/', include('tinymce.urls')),
    # path('events/', include('UpcomingEvents.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
