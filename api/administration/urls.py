from django.http import HttpResponse
from django.urls import path


def admin_view(request):
    return HttpResponse("ADMIN VIEW DO NOT ENTER")

urlpatterns = [
    path('', admin_view)
]