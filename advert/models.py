from django.db import models

# Create your models here.
from django.db import models
from section.models import List as Section


class List(models.Model):
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, related_name="advert_section")
    is_received = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
