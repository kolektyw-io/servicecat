from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from commons.models import SystemProperty


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login/login_form.html')
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            u = User.objects.get(email=username)
        except User.objects.DoesNotExist:
            return render(request, 'login/login_form_invalid.html')
        user = authenticate(request, username=u.username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("agent_home_view")
            else:
                return redirect("h")
        else:
            return render(request, 'login/login_form_invalid.html')
    else:
        return HttpResponse("Method not allowed", 407)


def logout_view(request):
    logout(request)
    return redirect("logged_out")


def profile(request):
    # FIXME: create profile view view
    pass


def register_view(request):
    # FIXME: create register view
    # register view contains functions required to register - or allowance
    # to register
    user_can_register, created = SystemProperty.objects.get_or_create(
        key='ninjacat.login.user_can_register')
    if created:
        user_can_register.value = "TRUE"
        user_can_register.save()

    if user_can_register.value == "TRUE":
        # FIXME logika rejestracji
        return render(request, "login/register.html")
    elif user_can_register.value == "INVITE_ONLY":
        # FIXME logika zaproszenia
        pass
    elif user_can_register.value == "CONFIRMATION_REQUIRED":
        # FIXME logika wymagania potwierdzenia przez użytkownika
        pass


def user_not_agent(request):
    return render(request, "errors/user_not_agent.html")


def user_not_authenticated(request):
    return render(request, "errors/user_not_authenticated.html")
