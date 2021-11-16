from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from commons.framework import AgentView


def agent_home_view(request):
    return render(request, 'bases/base_agent.html')


class AgentHomeView(AgentView):
    template_name = "agent/agent_std.html"


class AgentIssuesView(AgentView):
    template_name = "agent/agent_issues.html"


class AgentSettingsView(AgentView):
    template_name = "agent/agent_settings.html"
