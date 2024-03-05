from django.db import models
from project.models import List as Project
from space.models import List as Space

class List(models.Model):
    project = models.ForeignKey(Project, related_name="project_images", on_delete=models.SET_NULL, null=True, default=None)
    space = models.ForeignKey(Space, related_name="space_images", on_delete=models.SET_NULL, null=True, default=None)
    source = models.ImageField(upload_to='images/')