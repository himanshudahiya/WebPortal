from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lost_found/', include('lost_found.urls'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_URL)
	urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_URL)