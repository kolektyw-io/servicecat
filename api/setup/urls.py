from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path

from commons.models import SystemProperty


def setup_welcome(request):
    system_version, created = SystemProperty.objects.get_or_create(
        key='ninjacat.system.version')

    if not system_version.value:
        system_version.value = '0.0.1'
        system_version.save()
    return redirect("home")


def setup_migrate(request):
    return HttpResponse("Migration view")


urlpatterns = [
    path('setup/', setup_welcome, name='setup_start'),
    path('upgrade/', setup_migrate, name='setup_upgrade')
]