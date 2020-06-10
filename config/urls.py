from django.conf import settings
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from pathologists.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', home, name='home'),
    url(r'pathologists/', include('pathologists.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
