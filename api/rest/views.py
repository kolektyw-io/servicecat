import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def nologin(request):
    dct = {"status": True}
    return HttpResponse(json.dumps(dct))

@login_required
def loginrequired(request):
    dct = {"status": True}
    return HttpResponse(json.dumps(dct))
