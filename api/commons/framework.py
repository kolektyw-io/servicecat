from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class CommonView(TemplateView):
    context = {}

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.context['username'] = self.request.user.username
        self.context['user_first_name'] = self.request.user.first_name
        self.context['user_last_name'] = self.request.user.last_name


class AgentView(CommonView):
    template_name = ""

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        if not self.request.user.is_superuser:
            return redirect("error_user_not_an_agent")

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class ClientView(CommonView):
    template_name = ""

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        if self.request.user is None:
            return redirect("login_view")
