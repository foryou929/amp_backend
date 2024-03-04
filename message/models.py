from django.db import models
from section.models import List as Section
from django.conf import settings

class List(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="section_messages"
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="messages"
    )
    type = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    content = models.TextField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
