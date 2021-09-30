from django.db import models

from projects.models import Project


class PortalGroup(models.Model):
    group_name = models.CharField(max_length=100)
    group_icon = models.CharField(max_length=100)
    group_order = models.IntegerField(null=True)


class Form(models.Model):
    form_name = models.CharField(max_length=200)
    form_icon = models.CharField(max_length=100)
    related_project = models.ForeignKey(
        Project, on_delete=models.deletion.CASCADE
    )


class FormField(models.Model):
    form = models.ForeignKey(Form, on_delete=models.deletion.CASCADE)
