from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from semantic_backend import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "auth/", include("drf_social_oauth2.urls", namespace="drf")
    ),  # add this line to include the auth urls
]
# add at the last
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)/
