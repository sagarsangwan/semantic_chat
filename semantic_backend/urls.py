from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "auth/", include("drf_social_oauth2.urls", namespace="drf")
    ),  # add this line to include the auth urls
]
