from django.db import models
from django.conf import settings
from project.models import List as Project


class List(models.Model):
    project = models.ForeignKey(Project, related_name="project_sections", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sections", on_delete=models.CASCADE)
    step = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
