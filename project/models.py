from django.db import models
from django.conf import settings


class List(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="projects"
    )
    area = models.IntegerField(default=0)
    content_size = models.CharField(max_length=255)
    description = models.TextField()
    name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    project_period = models.IntegerField(default=0)
    recruitment_content = models.IntegerField(default=0)
    recruitment_number = models.IntegerField(default=0)
    recruitment_period = models.IntegerField(default=0)
    space_type = models.IntegerField(default=0)
    year_designation = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
