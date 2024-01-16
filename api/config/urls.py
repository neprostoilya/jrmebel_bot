from django.contrib import admin
from django.urls import path, include
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Users.urls', namespace='Users')),
    path('catalog/', include('Catalog.urls', namespace='Catalog')),
    path('order/', include('Order.urls', namespace='Order')),
    path('times/', include('Times.urls', namespace='Times')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)