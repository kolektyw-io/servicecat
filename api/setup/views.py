from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def setup_superuser(request):
    if User.objects.filter(is_superuser=True).count() > 0:
        # FIXME Prepare some nice alert window
        return HttpResponse("This form has been already used", 401)
    if request.method == "GET":
        return render(request, 'setup/setup_superuser.html')
    if request.method == "POST":
        User.objects.create_user(
            first_name=request.POST['username'],
            username=request.POST['email'],
            password=request.POST['password'],
            email=request.POST['email'],
            is_superuser=True
        )
        return redirect('home')
