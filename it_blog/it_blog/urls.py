from django.contrib import admin
from django.http import request
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", include("home.urls")),
    path("blog/", include("blog.urls")),
    path("user/", include("user.urls")),
    path("", lambda request: redirect("/home")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



