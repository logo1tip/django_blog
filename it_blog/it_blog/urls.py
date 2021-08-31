from django.contrib import admin
from django.http import request
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", include("home.urls")),
    path("", lambda request: redirect("/home/"))
]
