from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from project.models import List as ProjectList


class List(models.Model):
    user = models.ForeignKey(User, related_name="apply_lists", on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectList, related_name="apply_lists", on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
