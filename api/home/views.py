from django.conf import settings
from django.shortcuts import render, redirect
# Create your views here.
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

    anonymous_allowed, created = SystemProperty.objects.get_or_create(
        key='ninjacat.login.access'
    )

    if created:
        anonymous_allowed.value = "TRUE"
        anonymous_allowed.save()

    if anonymous_allowed.value == "FALSE":
        return redirect("register_view")
    else:
        if request.user.is_authenticated:
            if request.user.profile.is_agent:
                return redirect("agent_home_view")
        else:
            # FIXME
            pass
    # FIXME
    return render(request, 'login/login_form.html')


def logged_out(args):
    pass

