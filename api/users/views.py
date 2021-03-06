from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from commons.framework import CommonView
from commons.models import SystemProperty


def login_view(request):
    #TODO: Logowanie jest trochę wieśniackie
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
    #FIXME: create profile view view
    pass


def user_not_agent(request):
    return render(request, "errors/user_not_agent.html")


def user_not_authenticated(request):
    return render(request, "errors/user_not_authenticated.html")


class RegisterUserView(CommonView):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.user_can_register, created = SystemProperty.objects.get_or_create(
            key='ninjacat.login.user_can_register')
        if created:
            self.user_can_register.value = "TRUE"
            self.user_can_register.save()

    def get(self, request, *args, **kwargs):
        if self.user_can_register.value == "TRUE":
            return render(request, "login/register.html")
        elif self.user_can_register.value == "INVITE_ONLY":
            #FIXME dodaj logikę zaproszenia do rejestracji
            return render(request, "login/register_invite_only.html")



    def post(self, request, *args, **kwargs):
        name = self.request.POST.get("name")
        password = self.request.POST.get("password")
        email = self.request.POST.get("email")

        first_name = name.split(" ")[0]
        try:
            last_name = name.split(" ")[1]
        except IndexError:
            last_name = ""
        try:
            usr = User.objects.create_user(email, email, password)
            usr.is_active = False
            usr.save()

        except IntegrityError:
            return HttpResponse("500 already exists")

        if self.user_can_register.value == "CONFIRMATION_REQUIRED":
            # FIXME logika wymagania potwierdzenia przez użytkownika
            return render(request, "login/register_confirmation_required.html")
        else:
            # FIXME: logika wysyłania potwierdzenia rejestracji na e-mail
            return render(request, "login/register_confirmation_success.html")
