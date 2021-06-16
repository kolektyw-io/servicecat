from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import path

from commons.models import SystemProperty


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login/login_form.html')
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            u = User.objects.get(email=username)
        except User.DoesNotExist:
            return render(request, 'login/login_form_invalid.html')
        user = authenticate(request, username=u.username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Successful, {}'.format(request.user.username))
        else:
            return render(request, 'login/login_form_invalid.html')
    else:
        return HttpResponse("Method not allowed", 407)


def logout_view(request):
    logout(request)
    return redirect("logged_out")


def profile(request):
    #FIXME: create profile view view
    pass


def register_view(args):
    #FIXME: create register view
    # register view contains functions required to register - or allowance
    # to register
    user_can_register, created = SystemProperty.objects.get_or_create(
        key='ninjacat.login.user_can_register')
    if created:
        user_can_register.value = "TRUE"
        user_can_register.save()

    if user_can_register.value == "TRUE":
        #FIXME logika rejestracji
        pass
    elif user_can_register.value == "INVITE_ONLY":
        #FIXME logika zaproszenia
        pass
    elif user_can_register.value == "CONFIRMATION_REQUIRED":
        #FIXME logika wymagania potwierdzenia przez użytkownika
        pass

urlpatterns = [
    path("login/", login_view, name='login_view'),
    path("logout/", logout_view, name='logout_view'),
    path("register/", register_view, name='register_view'),
    path("profile/", profile, name='profile_view')
]
