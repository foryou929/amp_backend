from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from project.models import List as Project


class List(models.Model):
    sender = models.ForeignKey(
        User, related_name="message_sender", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User, related_name="message_receiver", on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project, related_name="message_project", on_delete=models.CASCADE
    )
    type = models.IntegerField()
    status = models.IntegerField()
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
