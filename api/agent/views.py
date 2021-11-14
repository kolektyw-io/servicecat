from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from commons.framework import AgentView


def agent_home_view(request):
    return render(request, 'bases/base_agent.html')


class AgentHomeView(AgentView):
    template_name = "agent/agent_std.html"
