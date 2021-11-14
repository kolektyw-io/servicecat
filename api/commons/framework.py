from django.shortcuts import redirect
from django.views.generic import View, TemplateView


class CommonView(TemplateView):
    pass


class AgentView(TemplateView):
    def setup(self, request, *args, **kwargs):
        super(self.setup(request, *args, **kwargs))
        if not self.request.user.is_superuser:
            return redirect("error_user_not_an_agent")


class ClientView(TemplateView):
    def setup(self, request, *args, **kwargs):
        super(self.setup(request, *args, **kwargs))
        if self.request.user is None:
            return redirect("login_view")



