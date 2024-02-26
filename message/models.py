from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from section.models import List as Section


class List(models.Model):
    section = models.ForeignKey(
        Section, related_name="messages", on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        User, related_name="sender", on_delete=models.CASCADE
    )
    type = models.IntegerField()
    status = models.IntegerField(default=0)
    content = models.TextField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
