from django.http import HttpResponse
from django.urls import path

from commons.framework import AdministratorView


def admin_view(request):
    return HttpResponse("ADMIN VIEW DO NOT ENTER")

class AdministrationHomeView(AdministratorView):
    template_name = "bases/base_admin.html"

urlpatterns = [

    path('', AdministrationHomeView.as_view(), name='administration_home_view')

]
