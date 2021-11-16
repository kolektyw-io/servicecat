from django.urls import path

from commons.framework import AgentView
from projects.models import Project


class MyProjectsView(AgentView):
    template_name = "agent/agent_projects.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, args, kwargs)
        self.context["projects"] = Project.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)


urlpatterns = [
    path("my/", MyProjectsView.as_view(), name='agent_projects_view')
]
