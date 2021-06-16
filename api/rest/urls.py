from django.urls import path

from rest.views import nologin, loginrequired

urlpatterns = [
    path('nologin', nologin),
    path('loginrequired', loginrequired),
]