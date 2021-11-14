from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def client_home_view(request):
    return HttpResponse("USER NOMRAL REQUEST")
