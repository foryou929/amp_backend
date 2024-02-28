from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from section.models import List as Section


class List(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="section_messages"
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messagfes"
    )
    type = models.IntegerField()
    status = models.IntegerField(default=0)
    content = models.TextField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
