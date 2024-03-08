from django.db import models
from django.conf import settings
from project.models import List as Project
from space.models import List as Space


class List(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name="project_sections")
    space = models.ForeignKey(Space, on_delete=models.SET_NULL, null=True, related_name="space_sections")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="sections")
    step = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
