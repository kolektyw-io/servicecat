from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from commons.models import SystemProperty


def home_view(request):
    system_version, created = SystemProperty.objects.get_or_create(
        key='ninjacat.system.version'
    )
    if not system_version.value:
        return redirect("setup_start")

    if not system_version.value == settings.LATEST_VERSION:
        print("Upgrade to {} required".format(system_version.value))
        return redirect("setup_upgrade")

    if User.objects.filter(is_superuser=True).count() == 0:
        return redirect("setup_superuser")

    return render(request, 'bases/base_client.html')


def logged_out(request):
    return render(request, 'login/logged_out.html')

