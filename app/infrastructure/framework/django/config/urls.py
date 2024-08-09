# mypy: disable-error-code=import-untyped

""" Register urls project global """

from django.conf import settings
from django.contrib import admin
from django.urls import path

from .app import api_v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api_v1.urls)
]
