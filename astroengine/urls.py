from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("persontoperson.urls")),
    path('match/', include("match.urls")),
    path('maplatest/', include('maplatest.urls')),
    path('multiples/', include("multiples.urls")),
    path('controlpanel/', include("controlpanel.urls")),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('displayers/', include('displayers.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
