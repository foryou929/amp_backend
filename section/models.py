from django.db import models
from django.contrib.auth.models import User
from project.models import List as Project


class List(models.Model):
    project = models.ForeignKey(
        Project, related_name="sections", on_delete=models.CASCADE
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    step = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
