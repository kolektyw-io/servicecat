from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def agent_home_view(request):
    return HttpResponse('agent home view')
